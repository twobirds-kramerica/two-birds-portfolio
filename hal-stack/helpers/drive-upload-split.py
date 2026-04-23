"""Split a large JSON-array file into per-record uploads to Google Drive.

Structural fix for RI-007: single-call base64 uploads via the Drive MCP's
`create_file` tool cannot handle files >~5-10 MB. Most large archives from
Claude's data export (conversations.json, projects.json, etc.) are top-
level JSON arrays where each element is self-contained and small.

This helper splits the array, groups elements into bounded-size batches
that fit comfortably in a single tool-argument payload, and emits one
upload plan per batch. The actual uploads happen via the Drive MCP
tool in the caller (Claude Code), not here — this script only plans
and stages. That separation keeps the script runnable from a plain
python interpreter without MCP credentials, and keeps the MCP-calling
logic in Claude's hands where it belongs.

Typical invocation (from Claude Code with re-authed Drive MCP):
    python hal-stack/helpers/drive-upload-split.py \\
        --input  'C:/Users/getkr/Downloads/.../conversations.json' \\
        --key    uuid \\
        --naming '{index:04d}_{uuid_short}_{name_slug}.json' \\
        --chunk-mb 3 \\
        --out-dir hal-stack/helpers/_staged/conversations \\
        --plan-json hal-stack/helpers/_staged/conversations/plan.json

Result: `_staged/conversations/` contains N staged JSON files each < chunk-mb,
and `plan.json` lists them with target Drive titles. Claude Code then reads
each staged file + calls mcp__claude_ai_Google_Drive__create_file per entry.

Status: RI-007 structural skeleton. Runnable standalone (stages files locally);
Drive-upload integration left to the caller after MCP re-auth.
"""
from __future__ import annotations
import argparse
import base64
import json
import re
import sys
from pathlib import Path
from typing import Any


def slugify(text: str, max_len: int = 48) -> str:
    """Lowercase, ASCII alnum + hyphens, truncated. Empty string -> 'untitled'."""
    if not text:
        return "untitled"
    s = text.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    if not s:
        return "untitled"
    return s[:max_len].rstrip("-")


def record_title(
    record: dict,
    index: int,
    key_field: str,
    naming_template: str,
) -> str:
    """Generate a target filename for a single JSON record."""
    uuid = str(record.get(key_field, f"rec{index:06d}"))
    uuid_short = uuid.replace("-", "")[:8] if uuid else f"rec{index:06d}"
    name = str(record.get("name") or record.get("title") or record.get("summary") or "")
    return naming_template.format(
        index=index,
        uuid=uuid,
        uuid_short=uuid_short,
        name=name,
        name_slug=slugify(name),
    )


def size_of(obj: Any) -> int:
    """Rough byte size of a JSON-serialised object."""
    return len(json.dumps(obj, ensure_ascii=False).encode("utf-8"))


def chunk_records(
    records: list[dict],
    chunk_mb: float,
    key_field: str,
    naming_template: str,
) -> list[list[tuple[int, str, dict]]]:
    """Group records into chunks whose serialised size stays under chunk_mb.

    Each output chunk is a list of (index, target_title, record) tuples.
    Per-record size is checked; an individual record larger than the cap
    gets its own chunk with a warning printed.
    """
    cap_bytes = int(chunk_mb * 1024 * 1024)
    chunks: list[list[tuple[int, str, dict]]] = []
    current: list[tuple[int, str, dict]] = []
    current_size = 0
    overhead = 2  # '[]' wrapper
    sep_overhead = 1  # ','

    for i, rec in enumerate(records):
        size = size_of(rec)
        title = record_title(rec, i, key_field, naming_template)
        if size > cap_bytes:
            print(
                f"WARN  record {i} ({title}) serialises to {size} bytes, "
                f"exceeds chunk cap {cap_bytes}. Emitting as its own chunk anyway."
            )
            if current:
                chunks.append(current)
                current = []
                current_size = 0
            chunks.append([(i, title, rec)])
            continue
        projected = current_size + size + (sep_overhead if current else 0) + overhead
        if projected > cap_bytes and current:
            chunks.append(current)
            current = []
            current_size = 0
        current.append((i, title, rec))
        current_size += size + (sep_overhead if current else 0)

    if current:
        chunks.append(current)
    return chunks


def stage_chunks(
    chunks: list[list[tuple[int, str, dict]]],
    out_dir: Path,
    one_record_per_file: bool,
) -> list[dict]:
    """Write chunk contents to disk and return an upload plan."""
    out_dir.mkdir(parents=True, exist_ok=True)
    plan: list[dict] = []
    for ci, chunk in enumerate(chunks):
        if one_record_per_file:
            for (rec_idx, title, rec) in chunk:
                path = out_dir / title
                path.write_text(
                    json.dumps(rec, ensure_ascii=False, indent=2),
                    encoding="utf-8",
                )
                plan.append({
                    "local_path": str(path),
                    "drive_title": title,
                    "record_indices": [rec_idx],
                    "size_bytes": path.stat().st_size,
                    "mime_type": "application/json",
                })
        else:
            group_title = f"batch_{ci:04d}_{chunk[0][0]:06d}_to_{chunk[-1][0]:06d}.json"
            path = out_dir / group_title
            path.write_text(
                json.dumps([rec for (_, _, rec) in chunk], ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            plan.append({
                "local_path": str(path),
                "drive_title": group_title,
                "record_indices": [idx for (idx, _, _) in chunk],
                "size_bytes": path.stat().st_size,
                "mime_type": "application/json",
            })
    return plan


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Split a large JSON-array file into upload-sized chunks.",
    )
    parser.add_argument(
        "--input", required=True, type=Path,
        help="Path to the source JSON file (must parse as a top-level array).",
    )
    parser.add_argument(
        "--key", default="uuid",
        help="Name of the unique-ID field in each record (default: uuid).",
    )
    parser.add_argument(
        "--naming",
        default="{index:04d}_{uuid_short}_{name_slug}.json",
        help="Python .format() template for per-record filenames. "
             "Fields: index, uuid, uuid_short, name, name_slug.",
    )
    parser.add_argument(
        "--chunk-mb", type=float, default=3.0,
        help="Target max size per chunk in MiB (default 3, safely under MCP arg limits).",
    )
    parser.add_argument(
        "--out-dir", required=True, type=Path,
        help="Local staging directory for split files (will be created).",
    )
    parser.add_argument(
        "--plan-json", required=True, type=Path,
        help="Where to write the upload plan JSON (consumed by the MCP caller).",
    )
    parser.add_argument(
        "--one-record-per-file", action="store_true",
        help="Instead of batching, emit one file per record (better for findability "
             "in Drive; trades file-count for per-record discoverability).",
    )
    parser.add_argument(
        "--encode-base64", action="store_true",
        help="Additionally emit base64-encoded content next to each staged file "
             "(speeds up MCP upload — create_file wants base64).",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Parse + plan only; do not write any files or plan.json.",
    )

    args = parser.parse_args(argv)

    if not args.input.is_file():
        print(f"ERROR: input not found: {args.input}", file=sys.stderr)
        return 2

    print(f"Reading {args.input} ...")
    try:
        with args.input.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: input is not valid JSON: {e}", file=sys.stderr)
        return 3

    if not isinstance(data, list):
        print(
            f"ERROR: input is not a top-level JSON array (got {type(data).__name__}).",
            file=sys.stderr,
        )
        return 4

    print(f"Parsed {len(data)} records. Chunking at {args.chunk_mb} MiB cap ...")
    chunks = chunk_records(data, args.chunk_mb, args.key, args.naming)
    print(
        f"Planned {len(chunks)} chunks "
        f"({'one-file-per-record' if args.one_record_per_file else 'batched'})."
    )

    if args.dry_run:
        total_size = sum(size_of([r for (_, _, r) in c]) for c in chunks)
        print(f"DRY RUN: would stage ~{total_size / 1024 / 1024:.1f} MiB to {args.out_dir}.")
        for ci, chunk in enumerate(chunks[:5]):
            print(f"  chunk {ci:03d}: {len(chunk)} records")
        if len(chunks) > 5:
            print(f"  ... {len(chunks) - 5} more chunks")
        return 0

    plan = stage_chunks(chunks, args.out_dir, args.one_record_per_file)

    if args.encode_base64:
        for entry in plan:
            local = Path(entry["local_path"])
            b64_path = local.with_suffix(local.suffix + ".b64")
            encoded = base64.b64encode(local.read_bytes()).decode("ascii")
            b64_path.write_text(encoded, encoding="ascii")
            entry["b64_path"] = str(b64_path)

    args.plan_json.parent.mkdir(parents=True, exist_ok=True)
    args.plan_json.write_text(
        json.dumps({"chunks": plan, "source": str(args.input)}, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote plan to {args.plan_json}. {len(plan)} upload entries.")
    print(
        "\nNext step (Claude Code, with re-authed Drive MCP): read the plan, "
        "then for each entry call mcp__claude_ai_Google_Drive__create_file with:\n"
        "  - title       = entry['drive_title']\n"
        "  - mimeType    = entry['mime_type']\n"
        "  - parentId    = <ID of target Drive folder>\n"
        "  - content     = base64 of local_path (or entry['b64_path'] if --encode-base64 used)\n"
        "\n"
        "Validate Drive scope first with a zero-content folder create; "
        "see RELIABILITY-ISSUES.md RI-007 for context."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

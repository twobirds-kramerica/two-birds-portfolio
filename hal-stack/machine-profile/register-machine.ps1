# register-machine.ps1
# Detects current machine specs and registers in machines.json
# Run: powershell -ExecutionPolicy Bypass -File register-machine.ps1
#
# STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
# Created: 2026-04-10 02:15 EST (Toronto)
# Confidence: MEDIUM — basic detection works, edge cases untested
# Known gaps: Storage type detection (SSD vs HDD) is a guess

$ErrorActionPreference = "Stop"

$jsonPath = Join-Path $PSScriptRoot "machines.json"

# Detect specs
$hostname = $env:COMPUTERNAME
$cpu = (Get-CimInstance Win32_Processor).Name.Trim()
$cores = (Get-CimInstance Win32_Processor).NumberOfCores
$ramGB = [math]::Round((Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1GB)
$os = (Get-CimInstance Win32_OperatingSystem).Caption
$osVer = (Get-CimInstance Win32_OperatingSystem).Version

$disks = Get-CimInstance Win32_DiskDrive | ForEach-Object {
    @{
        model = $_.Model.Trim()
        size_gb = [math]::Round($_.Size / 1GB)
        type = "unknown"
    }
}

# Prompt for nickname and role
$nickname = Read-Host "Machine nickname (e.g. EZbook, i5 Lenovo)"
$role = Read-Host "Role (primary / secondary / legacy / planned)"

# Build entry
$entry = @{
    id = "$($nickname.ToLower() -replace '\s+','-')-$(Get-Random -Maximum 999)"
    hostname = $hostname
    nickname = $nickname
    os = $os
    os_version = $osVer
    specs = @{
        cpu = $cpu
        cores = $cores
        ram_gb = $ramGB
        storage = $disks
    }
    role = $role
    status = "active"
    claude_code_installed = $null -ne (Get-Command claude -ErrorAction SilentlyContinue)
    claude_code_version = "unknown"
    node_version = if (Get-Command node -ErrorAction SilentlyContinue) { (node --version) } else { "not installed" }
    git_version = if (Get-Command git -ErrorAction SilentlyContinue) { (git --version) -replace "git version ","" } else { "not installed" }
    last_session = (Get-Date -Format "yyyy-MM-dd")
    local_paths = @{
        repo_root = "C:\twobirds\"
        scratch = $null
    }
    layer = "L1"
    notes = "Registered via register-machine.ps1 on $(Get-Date -Format 'yyyy-MM-dd')"
}

# Load existing or create new
if (Test-Path $jsonPath) {
    $data = Get-Content $jsonPath -Raw | ConvertFrom-Json

    # Check if hostname already registered
    $existing = $data.machines | Where-Object { $_.hostname -eq $hostname }
    if ($existing) {
        Write-Host "Machine '$hostname' already registered as '$($existing.nickname)'. Updating specs..." -ForegroundColor Yellow
        # Update in place
        $existing.specs = $entry.specs
        $existing.os = $entry.os
        $existing.os_version = $entry.os_version
        $existing.last_session = $entry.last_session
        $existing.node_version = $entry.node_version
        $existing.git_version = $entry.git_version
    } else {
        $data.machines += $entry
        Write-Host "Registered new machine: $nickname ($hostname)" -ForegroundColor Green
    }

    $data.last_updated = (Get-Date -Format "yyyy-MM-ddTHH:mm:sszzz")
} else {
    $data = @{
        schema_version = "1.0"
        last_updated = (Get-Date -Format "yyyy-MM-ddTHH:mm:sszzz")
        machines = @($entry)
    }
    Write-Host "Created new machines.json with $nickname" -ForegroundColor Green
}

$data | ConvertTo-Json -Depth 5 | Set-Content $jsonPath -Encoding UTF8
Write-Host "machines.json updated. Review and commit." -ForegroundColor Cyan

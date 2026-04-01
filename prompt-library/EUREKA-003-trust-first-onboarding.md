# 🔴 EUREKA-003 — Trust-First Onboarding
Date captured: April 1, 2026
Theme: Product
Shareability: 5
Personal flag: 🟡 Adaptable

## The Problem It Solves
When you build a digital product for anxious users — seniors, first-time tech users, people who have been scammed — a standard "Sign up and get started" flow creates immediate friction. The user sees a complex interface and closes the tab. Trust-first onboarding addresses this by showing a warm, simple overlay before the user sees any complexity. It answers three questions: What is this? Is it safe? What do I do first?

## Why It's A Eureka Moment
Most onboarding flows optimise for speed — get the user to the product as fast as possible. For anxious users, speed is the enemy. They need reassurance before action. The DCC onboarding overlay uses plain language, large text, a safety message ("This is free. Nothing will be downloaded. You cannot break anything."), and a single green button that says "I'm ready to start." The insight: for trust-sensitive audiences, the onboarding IS the product experience.

## The Hook (for social media)
"For anxious users, onboarding isn't a funnel — it's a safety blanket. Here's the 4-step overlay that changed how seniors interact with our platform."

## The Verbatim Prompt
```
Build a first-visit onboarding overlay for the Digital Confidence Centre.
Target audience: seniors 70+ who are afraid of technology.
4 steps, each one screen:
Step 1: "Welcome to the Digital Confidence Centre" — what this is in one sentence
Step 2: "This is completely free and safe" — safety reassurance, nothing downloads,
        you cannot break anything, your information stays private
Step 3: "Start with what matters to you" — show 3 module categories
        (Staying Safe, Staying Connected, Getting Things Done)
Step 4: "You're ready" — single green button: "I'm ready to start"
Large text. High contrast. One action per screen. No jargon.
Remember on return visits (localStorage flag). Dismissible but not aggressive.
```

## The Result
A 4-step full-screen overlay that appears on first visit to the DCC. Each step has one message and one action. The safety step explicitly addresses the three fears seniors express most: cost, downloads, and breaking things. Return visitors skip it automatically. The overlay reduced bounce rate from the home page and increased module starts.

## How To Adapt It
- Change the audience profile (anxious users exist in healthcare, finance, government)
- Replace the safety messages with whatever your users fear most
- Keep the one-action-per-screen principle — it works for any trust-sensitive context
- Use localStorage to track first visit — no backend needed
- The key insight: name the fears out loud. "You cannot break anything" is more powerful than "Easy to use"

# Grok Bot GTM Team

**A Grok-first GTM team, adapted and extended by Aditya Chouhan.**

[Start setup](setup-prompt.md) · [Complete copy/paste bundle](dist/grok-team-import.txt) · [All Bot instructions](agents/)

Grok Bot coordinates the team; specialists own outbound, content and conversations. Claude Code/Codex execution is optional and uses your configured route. No local CLI is required.

## Start

1. Create **Chief of Staff** in Grok Bot.
2. Paste the complete import bundle into its chat.
3. Answer the company, audience, tool, context, execution and review questions.
4. Choose a five-Bot outbound/content starter, or the full fifteen-Bot team.
5. Inspect the receipt; finish unsupported creation/room steps manually.
6. Run the [first draft-only job](examples/first-job.md).

## Team

Chief of Staff; Outbound Lead; Lead Sourcer; Outbound Copywriter; Sequences & Deliverability; Social Engagement; Reply Manager; Deal Reactivation; Head of Content; LinkedIn Writer; X Writer; YouTube Writer; Graphic Designer; Quality Reviewer; Revenue Analyst.

Outbound Room and Content Room include only selected members. Routines are off until explicitly requested.

## Improvements

- Five-Bot starter presets and a complete instruction bundle.
- Capability checks and manual fallback instead of assuming bot-creation tools exist.
- Setup reruns inspect existing Bots/rooms and preserve custom instructions.
- Explicit source, artifact revision, action approval and cost boundaries.
- Separate quality review and outcome measurement roles.
- Uncertain external outcomes stop for receipt checks before retry.
- Vendor-neutral connector mapping and manual assistant handoffs.

These are prompt-level behaviors, not technical connector isolation, automatic evidence-change detection or a runtime. The original role text's schedule/tool defaults are overridden by the appended operating rules and setup choices.

## Status and validation

The kit has **not been provisioned or behaviorally tested inside Grok**. Creation, rooms, routines and execution depend on your account's available capabilities. Examples are illustrative, not proof of installed Bots or revenue results.

Run `python3 scripts/validate.py` for structural checks. End users only copy/paste into Grok. See [operating templates](templates/operations.md) and [live validation checklist](guides/grok-validation.md).

## Credit

Based on Tim Scheuer's MIT-licensed [Grok Bot GTM team](https://github.com/timscheuerai/grokbot-gtm-team). Original role instructions are retained and adapted, with extended setup, shared rules, presets, quality and measurement roles by Aditya Chouhan. Upstream attribution is preserved in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). No endorsement or affiliation is implied.

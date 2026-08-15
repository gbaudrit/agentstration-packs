# Daily Life Assistant

> [!IMPORTANT]
> **Sample Pack** — This Pack demonstrates an orchestration pattern. Review and adapt it before real-world use.

**Audience:** Personal  
**Orchestration:** handoff

Route an everyday request to the most relevant declared specialist.

## What this Pack demonstrates

This Pack is an executable example of Agentstration's `handoff` orchestration. It installs its Agents, one published active Flow named `main`, and one conversational Entry named `main` into the namespace `agentstration.daily-life-assistant`.

## Try it

- Help me organize a busy week.
- My phone will not connect to my television.

## Requirements and limits

- The shared Model Profile `default/reasoning-default` must exist.
- Agent installation does not yet create Runtime revisions and deployments automatically.
- The Entry must be exposed in a Workplace Workspace after installation.
- The Pack uses no external tools and must not claim to have performed external actions.
- Outputs are model-generated; validate important decisions before acting on them.

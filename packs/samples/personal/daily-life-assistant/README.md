# Daily Life Assistant

> [!IMPORTANT]
> **Sample Pack** — This Pack demonstrates an orchestration pattern. Review and adapt it before real-world use.

**Audience:** Personal  
**Orchestration:** handoff

Route an everyday request to the most relevant declared specialist.

## What this Pack demonstrates

This Pack is an executable example of Agentstration's `handoff` orchestration. It installs its Agents, one published active Flow named `daily-life-assistant`, and one conversational Entry named `daily-life-assistant` into the namespace `agentstration.daily-life-assistant`.

## Try it

- Help me organize a busy week.
- My phone will not connect to my television.

## Requirements and limits

- Installation requires selecting an available Model Profile for the required `agent-model` binding. The selection is retained for this Pack identity; a fork requires its own selection.
- Agent installation does not yet create Runtime revisions and deployments automatically.
- The Entry must be exposed in a Workplace Workspace after installation.
- The Pack uses no external tools and must not claim to have performed external actions.
- Outputs are model-generated; validate important decisions before acting on them.

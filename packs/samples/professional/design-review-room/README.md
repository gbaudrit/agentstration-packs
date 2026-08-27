# Design Review Room

> [!IMPORTANT]
> **Sample Pack** — This Pack demonstrates an orchestration pattern. Review and adapt it before real-world use.

**Audience:** Professional  
**Orchestration:** groupChat

Run a bounded collaborative design review and record a final decision.

## What this Pack demonstrates

This Pack is an executable example of Agentstration's `groupChat` orchestration. It installs its Agents, one published active Flow named `design-review-room`, and one conversational Entry named `design-review-room` into the namespace `agentstration.design-review-room`.

## Try it

- Review whether this feature needs a workflow or orchestration.
- Challenge this API design and record a decision.

## Requirements and limits

- Installation requires selecting an available Model Profile for the required `agent-model` binding. The selection is retained for this Pack identity; a fork requires its own selection.
- Agent installation does not yet create Runtime revisions and deployments automatically.
- The Entry must be exposed in a Workplace Workspace after installation.
- The Pack uses no external tools and must not claim to have performed external actions.
- Outputs are model-generated; validate important decisions before acting on them.

# Weekend Planning Room

> [!IMPORTANT]
> **Sample Pack** — This Pack demonstrates an orchestration pattern. Review and adapt it before real-world use.

**Audience:** Personal  
**Orchestration:** groupChat

Build a balanced weekend plan through one bounded shared discussion.

## What this Pack demonstrates

This Pack is an executable example of Agentstration's `groupChat` orchestration. It installs its Agents, one published active Flow named `weekend-planning-room`, and one conversational Entry named `weekend-planning-room` into the namespace `agentstration.weekend-planning-room`.

## Try it

- Plan a relaxed weekend with a modest budget.
- Plan a rainy family weekend at home.

## Requirements and limits

- Installation requires selecting an available Model Profile for the required `agent-model` binding. The selection is retained for this Pack identity; a fork requires its own selection.
- Agent installation does not yet create Runtime revisions and deployments automatically.
- The Entry must be exposed in a Workplace Workspace after installation.
- The Pack uses no external tools and must not claim to have performed external actions.
- Outputs are model-generated; validate important decisions before acting on them.

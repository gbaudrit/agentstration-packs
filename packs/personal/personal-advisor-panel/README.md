# Personal Advisor Panel

**Audience:** Personal  
**Orchestration:** concurrent

Collect independent budget, practicality, and sustainability perspectives.

## What this Pack demonstrates

This Pack is an executable example of Agentstration's `concurrent` orchestration. It installs its Agents, one published active Flow named `main`, and one conversational Entry named `main` into the namespace `agentstration.personal-advisor-panel`.

## Try it

- Give me three perspectives on buying a new device.
- Review my idea for a home project.

## Requirements and limits

- The shared Model Profile `default/reasoning-default` must exist.
- Agent installation does not yet create Runtime revisions and deployments automatically.
- The Entry must be exposed in a Workplace Workspace after installation.
- The Pack uses no external tools and must not claim to have performed external actions.
- Outputs are model-generated; validate important decisions before acting on them.

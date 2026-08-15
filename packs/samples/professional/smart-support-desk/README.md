# Smart Support Desk

> [!IMPORTANT]
> **Sample Pack** — This Pack demonstrates an orchestration pattern. Review and adapt it before real-world use.

**Audience:** Professional  
**Orchestration:** handoff

Qualify a support request and hand it to the appropriate specialist.

## What this Pack demonstrates

This Pack is an executable example of Agentstration's `handoff` orchestration. It installs its Agents, one published active Flow named `smart-support-desk`, and one conversational Entry named `smart-support-desk` into the namespace `agentstration.smart-support-desk`.

## Try it

- A user cannot start the application.
- A customer has a question about an invoice.

## Requirements and limits

- The shared Model Profile `default/reasoning-default` must exist.
- Agent installation does not yet create Runtime revisions and deployments automatically.
- The Entry must be exposed in a Workplace Workspace after installation.
- The Pack uses no external tools and must not claim to have performed external actions.
- Outputs are model-generated; validate important decisions before acting on them.

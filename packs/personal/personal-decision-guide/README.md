# Personal Decision Guide

**Audience:** Personal  
**Orchestration:** sequential

Turn an everyday decision into a clear, balanced recommendation.

## What this Pack demonstrates

This Pack is an executable example of Agentstration's `sequential` orchestration. It installs its Agents, one published active Flow named `main`, and one conversational Entry named `main` into the namespace `agentstration.personal-decision-guide`.

## Try it

- Help me choose between repairing and replacing an appliance.
- Compare two ideas for my weekend.

## Requirements and limits

- The shared Model Profile `default/reasoning-default` must exist.
- Agent installation does not yet create Runtime revisions and deployments automatically.
- The Entry must be exposed in a Workplace Workspace after installation.
- The Pack uses no external tools and must not claim to have performed external actions.
- Outputs are model-generated; validate important decisions before acting on them.

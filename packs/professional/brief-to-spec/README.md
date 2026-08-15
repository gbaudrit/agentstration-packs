# Brief to Spec

**Audience:** Professional  
**Orchestration:** sequential

Turn a product or engineering brief into a reviewed implementation specification.

## What this Pack demonstrates

This Pack is an executable example of Agentstration's `sequential` orchestration. It installs its Agents, one published active Flow named `main`, and one conversational Entry named `main` into the namespace `agentstration.brief-to-spec`.

## Try it

- Specify a price-monitoring automation.
- Turn these product notes into an implementation brief.

## Requirements and limits

- The shared Model Profile `default/reasoning-default` must exist.
- Agent installation does not yet create Runtime revisions and deployments automatically.
- The Entry must be exposed in a Workplace Workspace after installation.
- The Pack uses no external tools and must not claim to have performed external actions.
- Outputs are model-generated; validate important decisions before acting on them.

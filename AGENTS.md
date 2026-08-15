# Agent instructions

This repository contains official Agentstration Pack source, not product runtime code.

- Preserve the `agentstration.io/v1` envelope and current Agentstration contracts.
- Keep Personal, Professional, and Universal as metadata audiences, never separate Pack kinds.
- Keep Sample, Template, and Standard as metadata purposes, never separate Pack kinds or lifecycle implementations.
- Store published Packs under `packs/<purpose>/<audience>/<name>` and keep both metadata axes aligned with the path.
- Never add secrets, personal data, generated ZIP files, or undeclared external integrations.
- Unqualified resource references must resolve inside the Pack namespace. External references require an explicit namespace.
- Every Flow must be published and active; every Entry must bind to a contained Flow.
- Keep orchestration bounded and preserve the documented behavior of Sequential, Concurrent, Handoff, Group Chat, and Magentic.
- Update README, CHANGELOG, validation, and generated catalog metadata together.
- Do not assert exact LLM prose in tests. Validate structure, participants, routing, bounds, and terminal state.

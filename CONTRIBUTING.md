# Contributing

Each Pack lives under `packs/<purpose>/<audience>/<name>`, for example `packs/samples/professional/brief-to-spec`.

A contribution must include:

- `pack.yaml`, `README.md`, and `CHANGELOG.md`;
- every resource listed exactly once in `definition.resources`;
- an explicit `metadata.audience` matching its collection;
- an explicit `metadata.purpose` (`sample`, `template`, or `standard`) matching its collection;
- lowercase kebab-case publisher, Pack, and resource names;
- explicit namespaces for references outside the Pack;
- no credentials, personal data, generated archives, or external-action claims;
- logical Pack bindings for external Model Profiles and Secrets instead of hard-coded environment-specific references;
- bounded orchestration settings and a published active Flow;
- an Entry bound to a Flow contained in the same Pack.

For a Sample, the primary Flow and Entry must use the Pack's `metadata.name`. Their files follow the same convention: `flows/<pack-name>.yaml` and `entries/<pack-name>.yaml`. Additional resources use a descriptive `<pack-name>-<role>` name.

Declare install-time resource selections in `definition.bindings`. Use the required `agent-model` binding when every Agent shares one Model Profile, then reference it as `modelProfile: { binding: agent-model }`. Use role-specific bindings only when independent selections are part of the Pack's behavior. Binding declarations must be used, and secret values must never be stored in Pack source or generated archives.

Run all validation, unit test, catalog, and deterministic build commands from the root before opening a pull request.

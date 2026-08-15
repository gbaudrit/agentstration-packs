# Contributing

Each Pack lives under `packs/personal`, `packs/professional`, or `packs/universal`.

A contribution must include:

- `pack.yaml`, `README.md`, and `CHANGELOG.md`;
- every resource listed exactly once in `spec.resources`;
- an explicit `metadata.audience` matching its collection;
- lowercase kebab-case publisher, Pack, and resource names;
- explicit namespaces for references outside the Pack;
- no credentials, personal data, generated archives, or external-action claims;
- bounded orchestration settings and a published active Flow;
- an Entry bound to a Flow contained in the same Pack.

Run all validation and deterministic build commands from the root before opening a pull request.

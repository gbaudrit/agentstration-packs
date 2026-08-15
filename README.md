# Agentstration Packs

Official, versioned Packs for [Agentstration](https://github.com/gbaudrit/agentstration).

## Repository structure

Packs are organized first by purpose, then by audience:

```text
packs/
  samples/
    personal/
    professional/
    universal/
  templates/
  standard/
```

- **Sample** — demonstrative Packs for learning and evaluating an orchestration.
- **Template** — starting points intended to be forked and customized.
- **Standard** — regular Packs without a special usage designation.

`standard` is the compatibility default when purpose is omitted. Sample and Template Packs must declare their purpose explicitly and are visually identified by consumers.

## Audiences

- **Personal** — everyday decisions, organization, leisure, and personal projects.
- **Professional** — governed work, product development, support, architecture, and delivery.
- **Universal** — experiences intentionally suitable in both contexts.

All audiences and purposes use the same Pack contract and installation lifecycle. They are discovery metadata, not separate runtimes or security boundaries.

## Initial sample coverage

| Strategy | Personal | Professional |
| --- | --- | --- |
| Sequential | `personal-decision-guide` | `brief-to-spec` |
| Concurrent | `personal-advisor-panel` | `expert-panel` |
| Handoff | `daily-life-assistant` | `smart-support-desk` |
| Group Chat | `weekend-planning-room` | `design-review-room` |
| Magentic | `event-planner` | `adaptive-delivery-plan` |

## Validate and build

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_packs.py
python scripts/generate_catalog.py --check
python scripts/build_packs.py --output dist
```

The repository validator checks catalog conventions and orchestration references. Agentstration preview/install remains the authoritative product validation boundary.

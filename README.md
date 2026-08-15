# Agentstration Packs

Official, versioned Packs for [Agentstration](https://github.com/gbaudrit/agentstration).

## Collections

- **Personal** — everyday decisions, organization, leisure, and personal projects.
- **Professional** — governed work, product development, support, architecture, and delivery.
- **Universal** — experiences intentionally suitable in both contexts.

All collections use the same Pack contract and installation lifecycle. Audience is discovery metadata, not a separate runtime or security boundary.

## Initial orchestration coverage

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

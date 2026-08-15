from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "catalog.json"


def generate() -> str:
    packs = []
    for path in sorted((ROOT / "packs").glob("*/*/pack.yaml")):
        manifest = yaml.safe_load(path.read_text(encoding="utf-8"))
        metadata = manifest["metadata"]
        tags = metadata.get("tags", [])
        strategy = next((tag for tag in tags if tag in {"sequential", "concurrent", "handoff", "group-chat", "magentic"}), None)
        packs.append({
            "audience": metadata["audience"],
            "categories": metadata.get("categories", []),
            "description": metadata.get("description"),
            "displayName": metadata.get("displayName", metadata["name"]),
            "name": metadata["name"],
            "publisher": metadata["publisher"],
            "resourceCount": len(manifest["spec"].get("resources", [])),
            "source": str(path.parent.relative_to(ROOT)).replace("\\", "/"),
            "strategy": strategy,
            "tags": tags,
            "version": metadata["version"],
        })
    value = {
        "apiVersion": "agentstration.io/catalog/v1",
        "kind": "PackCatalog",
        "metadata": {"name": "official", "publisher": "agentstration"},
        "spec": {"packs": packs},
    }
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    content = generate()
    if args.check:
        if not TARGET.exists() or TARGET.read_text(encoding="utf-8") != content:
            raise SystemExit("catalog.json is not up to date; run scripts/generate_catalog.py")
        print("catalog.json is up to date.")
        return 0
    TARGET.write_text(content, encoding="utf-8", newline="\n")
    print(f"Wrote {TARGET.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

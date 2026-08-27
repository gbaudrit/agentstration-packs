from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TAG = re.compile(
    r"^pack/(?P<name>[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)/v"
    r"(?P<version>\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?)$"
)


@dataclass(frozen=True)
class PackRelease:
    name: str
    version: str
    manifest: Path


def resolve_release(tag: str, root: Path = ROOT) -> PackRelease:
    match = TAG.fullmatch(tag)
    if match is None:
        raise ValueError("release tag must use pack/<name>/v<semver>")

    tag_name = match.group("name")
    tag_version = match.group("version")
    manifests = sorted((root / "packs").glob(f"*/*/{tag_name}/pack.yaml"))
    if not manifests:
        raise ValueError(f"unknown Pack in release tag: {tag_name}")
    if len(manifests) > 1:
        locations = ", ".join(str(path.relative_to(root)) for path in manifests)
        raise ValueError(f"Pack name is ambiguous across manifests: {locations}")

    manifest = manifests[0]
    document = yaml.safe_load(manifest.read_text(encoding="utf-8"))
    metadata = document.get("metadata") if isinstance(document, dict) else None
    if not isinstance(metadata, dict):
        raise ValueError(f"{manifest.relative_to(root)} has no metadata object")

    metadata_name = metadata.get("name")
    metadata_version = metadata.get("version")
    if metadata_name != tag_name:
        raise ValueError(
            f"release tag names Pack '{tag_name}', but metadata.name is '{metadata_name}'"
        )
    if metadata_version != tag_version:
        raise ValueError(
            f"release tag version '{tag_version}' does not match metadata.version "
            f"'{metadata_version}' for Pack '{tag_name}'"
        )

    return PackRelease(tag_name, tag_version, manifest)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tag", required=True)
    args = parser.parse_args()
    try:
        release = resolve_release(args.tag)
    except ValueError as error:
        parser.error(str(error))
    print(f"name={release.name}")
    print(f"version={release.version}")
    print(f"manifest={release.manifest.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

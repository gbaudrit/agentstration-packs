from __future__ import annotations

import argparse
import hashlib
import shutil
import tempfile
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PACKS = ROOT / "packs"
CANONICAL_TIME = (2026, 1, 1, 0, 0, 0)


def pack_sources(selected: str | None) -> list[Path]:
    values = sorted(PACKS.glob("*/*/*/pack.yaml"))
    if selected:
        values = [path for path in values if path.parent.name == selected]
        if not values:
            raise SystemExit(f"Unknown Pack: {selected}")
    return values


def archive_bytes(pack_file: Path) -> bytes:
    root = pack_file.parent
    manifest = yaml.safe_load(pack_file.read_text(encoding="utf-8"))
    version = manifest["metadata"]["version"]
    name = manifest["metadata"]["name"]
    included = [
        path for path in root.rglob("*")
        if path.is_file() and "tests" not in path.relative_to(root).parts
    ]
    with tempfile.SpooledTemporaryFile() as stream:
        with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path in sorted(included, key=lambda value: str(value.relative_to(root)).replace("\\", "/")):
                relative = str(path.relative_to(root)).replace("\\", "/")
                info = zipfile.ZipInfo(relative, CANONICAL_TIME)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        stream.seek(0)
        return stream.read(), name, version


def build(output: Path, selected: str | None) -> dict[str, str]:
    output.mkdir(parents=True, exist_ok=True)
    hashes: dict[str, str] = {}
    for pack_file in pack_sources(selected):
        content, name, version = archive_bytes(pack_file)
        target = output / f"{name}-{version}.pack.zip"
        target.write_bytes(content)
        hashes[target.name] = hashlib.sha256(content).hexdigest()
        print(f"{target.relative_to(ROOT) if target.is_relative_to(ROOT) else target}  {hashes[target.name]}")
    return hashes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    parser.add_argument("--pack")
    parser.add_argument("--verify-deterministic", action="store_true")
    args = parser.parse_args()
    first = build(args.output, args.pack)
    if args.verify_deterministic:
        with tempfile.TemporaryDirectory() as directory:
            second = build(Path(directory), args.pack)
        if first != second:
            raise SystemExit("Deterministic build verification failed.")
        print("Deterministic build verification succeeded.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

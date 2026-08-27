from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import resolve_pack_release


class PackReleaseResolutionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.manifest = self.root / "packs" / "samples" / "professional" / "demo-pack" / "pack.yaml"
        self.manifest.parent.mkdir(parents=True)
        self.manifest.write_text(
            "metadata:\n  name: demo-pack\n  version: 1.2.3\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def test_release_is_resolved_from_manifest_metadata(self) -> None:
        release = resolve_pack_release.resolve_release("pack/demo-pack/v1.2.3", self.root)

        self.assertEqual("demo-pack", release.name)
        self.assertEqual("1.2.3", release.version)
        self.assertEqual(self.manifest, release.manifest)

    def test_tag_version_must_match_manifest_metadata(self) -> None:
        with self.assertRaisesRegex(ValueError, "does not match metadata.version"):
            resolve_pack_release.resolve_release("pack/demo-pack/v1.2.4", self.root)

    def test_tag_must_use_release_convention(self) -> None:
        with self.assertRaisesRegex(ValueError, "pack/<name>/v<semver>"):
            resolve_pack_release.resolve_release("demo-pack/v1.2.3", self.root)

    def test_tag_must_reference_an_existing_pack(self) -> None:
        with self.assertRaisesRegex(ValueError, "unknown Pack"):
            resolve_pack_release.resolve_release("pack/missing/v1.2.3", self.root)


if __name__ == "__main__":
    unittest.main()

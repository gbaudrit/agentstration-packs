from __future__ import annotations

import unittest

from scripts import validate_packs


class PackBindingValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.pack_file = validate_packs.ROOT / "pack.yaml"

    def test_valid_model_profile_binding(self) -> None:
        errors: list[str] = []
        declarations = validate_packs.validate_binding_declarations(
            {
                "bindings": [
                    {
                        "name": "agent-model",
                        "targetKind": "modelProfile",
                        "displayName": "Agent model",
                        "required": True,
                    }
                ]
            },
            self.pack_file,
            errors,
        )

        self.assertEqual({"agent-model": "modelProfile"}, declarations)
        self.assertEqual([], errors)

    def test_duplicate_binding_is_rejected(self) -> None:
        errors: list[str] = []
        validate_packs.validate_binding_declarations(
            {
                "bindings": [
                    {"name": "agent-model", "targetKind": "modelProfile"},
                    {"name": "agent-model", "targetKind": "modelProfile"},
                ]
            },
            self.pack_file,
            errors,
        )

        self.assertTrue(any("duplicate binding declaration" in error for error in errors))

    def test_invalid_name_and_target_kind_are_rejected(self) -> None:
        errors: list[str] = []
        validate_packs.validate_binding_declarations(
            {
                "bindings": [
                    {"name": "-invalid", "targetKind": "modelProfile"},
                    {"name": "agent-model", "targetKind": "provider"},
                ]
            },
            self.pack_file,
            errors,
        )

        self.assertTrue(any(".name must be" in error for error in errors))
        self.assertTrue(any(".targetKind must be" in error for error in errors))

    def test_only_exact_binding_objects_are_placeholders(self) -> None:
        references = validate_packs.collect_binding_references(
            {
                "modelProfile": {"binding": "agent-model"},
                "ignored": {"binding": "not-a-placeholder", "extra": True},
                "nested": [{"binding": "secret-token"}],
            }
        )

        self.assertEqual(["agent-model", "secret-token"], references)


if __name__ == "__main__":
    unittest.main()

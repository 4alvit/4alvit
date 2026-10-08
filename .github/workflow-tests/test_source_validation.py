"""Exercise the profile repository's source-only validation boundaries."""

import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "source_validation", ROOT / "scripts/validate-source.py"
)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class SourceValidationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)

    def test_discovery_skips_exclusions_ignored_files_and_symlinks(self):
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        (self.root / "source.py").write_text("value = 1\n")
        (self.root / "ignored.py").write_text("value = 2\n")
        (self.root / ".gitignore").write_text("ignored.py\n")
        (self.root / "cache").mkdir()
        (self.root / "cache/hidden.py").write_text("value = 3\n")
        (self.root / "alias.py").symlink_to(self.root / "source.py")
        found = [name for name, _ in validator.source_paths(self.root, ["cache"])]
        self.assertEqual(found, ["source.py"])

    def test_python_failure_location_does_not_include_source_values(self):
        path = self.root / "invalid.py"
        path.write_text("fixture_private_value = (\n")
        with self.assertRaises(SyntaxError) as caught:
            validator.validate_file(self.root, path.name, path)
        message = validator.error_location(path.name, caught.exception)
        self.assertEqual(message, "invalid.py:1: SyntaxError")
        self.assertNotIn("fixture_private_value", message)

    def test_json_failure_does_not_echo_configuration(self):
        path = self.root / "invalid.json"
        path.write_text('{"synthetic_secret": fixture_private_value}')
        with self.assertRaises(ValueError) as caught:
            validator.validate_file(self.root, path.name, path)
        message = validator.error_location(path.name, caught.exception)
        self.assertNotIn("fixture_private_value", message)
        self.assertNotIn("synthetic_secret", message)
        self.assertTrue(message.startswith("invalid.json:1:"))

    def test_yaml_tags_are_parsed_without_constructing_python_objects(self):
        path = self.root / "config.yaml"
        path.write_text("value: !!python/object:missing_module.Fixture {}\n")
        self.assertEqual(validator.validate_file(self.root, path.name, path), ".yaml")

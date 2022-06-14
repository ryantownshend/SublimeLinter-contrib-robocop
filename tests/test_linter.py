"""Test the linter.

https://stackoverflow.com/questions/8658043/how-to-mock-an-import
"""
import re
import json
import unittest
import sys
from unittest.mock import Mock
sys.modules["SublimeLinter.lint"] = Mock()
import linter  # noqa


def load_data():
    """Load the test data."""
    with open("tests/linter_test_data.json", "r", encoding="utf-8") as reader:
        return json.load(reader)


class TestLinter(unittest.TestCase):
    """Test the linter."""

    def test_regex_pattern(self):
        """Test the linter's regex pattern."""
        data = load_data()
        pattern = re.compile(linter.PATTERN)
        result = pattern.match(data["error"])

        # filename, line, col, warning, error, code, message
        # self.assertEqual(
        #     result.group("filename"),
        #     "filename"
        # )
        self.assertEqual(
            result.group("line"),
            "11"
        )
        self.assertEqual(
            result.group("col"),
            "1"
        )
        self.assertEqual(
            result.group("error"),
            "E"
        )
        self.assertEqual(
            result.group("code"),
            "0313"
        )
        self.assertEqual(
            result.group("message"),
            "Test case name should not be empty (test-case-name-is-empty)"
        )

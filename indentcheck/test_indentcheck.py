#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Kanato Aketagawa
# SPDX-License-Identifier: BSD-3-Clause

import unittest
import subprocess
from pathlib import Path


COMMAND = Path(__file__).resolve().parent / "indentcheck"


class TestIndentcheck(unittest.TestCase):

    def run_check(self, source):
        return subprocess.run(
            [str(COMMAND)],
            input=source,
            text=True,
            capture_output=True
        )

    def test_correct_indent(self):
        result = self.run_check(
            'def hello():\n'
            '    print("Hello")\n'
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn(
            "No indentation errors found.",
            result.stderr
        )

    def test_wrong_indent(self):
        result = self.run_check(
            'def hello():\n'
            '  print("Hello")\n'
        )

        self.assertEqual(result.returncode, 1)
        self.assertIn("Line 2:", result.stderr)
        self.assertIn("1 indentation error(s) found.", result.stderr)

    def test_tab_indent(self):
        result = self.run_check(
            'def hello():\n'
            '\tprint("Hello")\n'
        )

        self.assertEqual(result.returncode, 1)
        self.assertIn("Tab detected.", result.stderr)

    def test_multiple_errors(self):
        result = self.run_check(
            'def hello():\n'
            '  print("Hello")\n'
            '   print("World")\n'
        )

        self.assertEqual(result.returncode, 1)
        self.assertIn("2 indentation error(s) found.", result.stderr)


if __name__ == "__main__":
    unittest.main()

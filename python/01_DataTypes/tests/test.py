"""
File:
    python/00_Introduction/tests/test.py
"""

"""
DO NOT MODIFY THIS FILE. TEST USE ONLY.
"""

from io import StringIO
import sys
import unittest

class TestBench(unittest.TestCase):

    def test_exercise_a(self):
        # Capture output of print statement.
        captured_output = StringIO()
        sys.stdout = captured_output

        # Restore original stdout.
        sys.stdout = sys.__stdout__

        # Assert.
        actual = captured_output.getvalue().strip()
        expected = "Hello, World"
        self.assertEqual(actual, expected)

if __name__=='__main__':
    unittest.main()

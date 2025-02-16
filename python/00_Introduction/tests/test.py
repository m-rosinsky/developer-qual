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

    def test_00a(self):
        # Capture output of print statement.
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call function.
        print("Hello, World")

        # Restore original stdout.
        sys.stdout = sys.__stdout__

        # Assert.
        self.assertEqual(captured_output.getvalue().strip(), "Hello, World")

if __name__=='__main__':
    unittest.main()

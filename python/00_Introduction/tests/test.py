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

from exercises.exercise_a import hello_world

class TestBench(unittest.TestCase):

    def test_exercise_a(self):
        # Capture output of print statement.
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call function.
        hello_world()

        # Restore original stdout.
        sys.stdout = sys.__stdout__

        # Assert.
        actual = captured_output.getvalue().strip()
        expected = "Hello, World"
        self.assertEqual(actual, expected)

    def test_exercise_b(self):
        from exercises.exercise_b import commenting_out

        # Capture output of print statements.
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call function.
        commenting_out()

        # Restore original stdout.
        sys.stdout = sys.__stdout__
        
        # Check output.
        actual_output = captured_output.getvalue().strip().splitlines()
        self.assertIn('a', actual_output)
        self.assertNotIn('b', actual_output)
        self.assertIn('c', actual_output)

if __name__=='__main__':
    unittest.main()

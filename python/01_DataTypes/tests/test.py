"""
File:
    python/01_DataTypes/tests/test.py
"""

"""
DO NOT MODIFY THIS FILE. TEST USE ONLY.
"""

from io import StringIO
import sys
import unittest

def trace_locals(frame, event, arg):
    """
    We use this function to trace local variables.
    """
    if event == "return":
        locals_dict = frame.f_locals
        if 'age' in locals_dict and 'name' in locals_dict:
            trace_locals.vars = (locals_dict['age'], locals_dict['name'])
    return trace_locals

class TestBench(unittest.TestCase):

    def test_exercise_a(self):
        from exercises.exercise_a import declare_and_print

        # Capture output of print statement.
        captured_output = StringIO()
        sys.stdout = captured_output

        # Set tracing to capture local variables.
        trace_locals.vars = None
        sys.settrace(trace_locals)

        # Call function.
        declare_and_print()

        # Reset trace.
        sys.settrace(None)

        # Restore original stdout.
        sys.stdout = sys.__stdout__

        # Check output
        actual_output = captured_output.getvalue().strip().splitlines()
        self.assertEqual(actual_output, ["25", "John Doe"])

        # Check locals
        self.assertIsNotNone(trace_locals.vars)
        age, name = trace_locals.vars
        self.assertEqual(age, 25)
        self.assertEqual(name, "John Doe")

    def test_exercise_b1(self):
        from exercises.exercise_b import integer_math

        # Capture output of print statement.
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call function.
        integer_math()

        # Restore original stdout.
        sys.stdout = sys.__stdout__

        # Get output.
        actual_output = captured_output.getvalue().strip().splitlines()

        # Assert.
        self.assertEqual(len(actual_output), 4, f"Required 4 print statements, received {len(actual_output)}")
        self.assertEqual(actual_output[0], '12', f"Got {actual_output[0]} for x + y, expected 12")
        self.assertEqual(actual_output[1], '4', f"Got {actual_output[1]} for x - y, expected 4")
        self.assertEqual(actual_output[2], '32', f"Got {actual_output[2]} for x * y, expected 32")
        self.assertEqual(actual_output[3], '2.0', f"Got {actual_output[3]} for x / y, expected 2.0")

    def test_exercise_b2(self):
        from exercises.exercise_b import advanced_integer_math

        # Capture output of print statement.
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call function.
        advanced_integer_math()

        # Restore original stdout.
        sys.stdout = sys.__stdout__

        # Check output.
        actual_output = captured_output.getvalue().strip().splitlines()

        # Assert.
        self.assertEqual(len(actual_output), 3, f"Required 3 print statements, received {len(actual_output)}")
        self.assertEqual(actual_output[0], '3', f"Got {actual_output[0]} for 17 // 5, expected 3")
        self.assertEqual(actual_output[1], '2', f"Got {actual_output[1]} for 17 % 5, expected 2")
        self.assertEqual(actual_output[2], '1419857', f"Got {actual_output[2]} for 17 ** 5, expected 1419857")

    def test_exercise_b3(self):
        from exercises.exercise_b import mixed_operations

        # Capture output of print statement.
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call function.
        mixed_operations()

        # Restore original stdout.
        sys.stdout = sys.__stdout__

        # Check output.
        actual_output = captured_output.getvalue().strip().splitlines()

        # Assert.
        self.assertEqual(len(actual_output), 1, f"Required 1 print statement, received {len(actual_output)}")
        self.assertEqual(actual_output[0], '34', f"Got {actual_output[0]}, expected 34")

    def test_exercise_b4(self):
        from exercises.exercise_b import string_operations

        # Capture output of print statement.
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call function.
        string_operations()

        # Restore original stdout.
        sys.stdout = sys.__stdout__

        # Check output.
        actual_output = captured_output.getvalue().strip().splitlines()

        # Assert.
        self.assertEqual(len(actual_output), 2, f"Required 2 print statements, received {len(actual_output)}")
        self.assertEqual(actual_output[0], 'hellohellohello', f"Got {actual_output[0]} for 'hello' * 3, expected 'hellohellohello'")
        self.assertEqual(actual_output[1], 'hellohello world', f"Got {actual_output[1]} for 'hello' * 2 + ' world', expected 'hellohello world'")

if __name__=='__main__':
    unittest.main()
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

if __name__=='__main__':
    unittest.main()

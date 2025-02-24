"""
File:
    python/02_ControlFlow/tests/test.py
"""

"""
DO NOT MODIFY THIS FILE. TEST USE ONLY.
"""

from io import StringIO
import sys
import unittest

class TestBench(unittest.TestCase):

    def test_exercise_a1(self):
        from exercises.exercise_a import compare_equals

        # Capture output of print statement.
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call function.
        compare_equals()

        # Restore original stdout.
        sys.stdout = sys.__stdout__

        # Check output.
        actual_output = captured_output.getvalue().strip().splitlines()
        self.assertEqual(len(actual_output), 1, f"Required 1 print statement, received {len(actual_output)}")
        self.assertEqual(actual_output[0], 'True', f"Got {actual_output[0]}, expected 'True'")

    def test_exercise_a2(self):
        from exercises.exercise_a import compare_not_equals

        # Capture output of print statement.
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call function.
        compare_not_equals()

        # Restore original stdout.
        sys.stdout = sys.__stdout__

        # Check output.
        actual_output = captured_output.getvalue().strip().splitlines()
        self.assertEqual(len(actual_output), 1, f"Required 1 print statement, received {len(actual_output)}")
        self.assertEqual(actual_output[0], 'True', f"Got {actual_output[0]}, expected 'True'")

    def test_exercise_a3(self):
        from exercises.exercise_a import compare_greater

        # Capture output of print statement.
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call function.
        compare_greater()

        # Restore original stdout.
        sys.stdout = sys.__stdout__

        # Check output.
        actual_output = captured_output.getvalue().strip().splitlines()
        self.assertEqual(len(actual_output), 1, f"Required 1 print statement, received {len(actual_output)}")
        self.assertEqual(actual_output[0], 'True', f"Got {actual_output[0]}, expected 'True'")

    def test_exercise_a4(self):
        from exercises.exercise_a import compare_with_calculation

        # Capture output of print statement.
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call function.
        compare_with_calculation()

        # Restore original stdout.
        sys.stdout = sys.__stdout__

        # Check output.
        actual_output = captured_output.getvalue().strip().splitlines()
        self.assertEqual(len(actual_output), 1, f"Required 1 print statement, received {len(actual_output)}")
        self.assertEqual(actual_output[0], 'True', f"Got {actual_output[0]}, expected 'True'")

    # New test cases for exercise_b.py
    def test_exercise_b1(self):
        from exercises.exercise_b import check_temperature

        # Capture output of print statement.
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call function.
        check_temperature()

        # Restore original stdout.
        sys.stdout = sys.__stdout__

        # Check output.
        actual_output = captured_output.getvalue().strip().splitlines()
        self.assertEqual(len(actual_output), 1, f"Required 1 print statement, received {len(actual_output)}")
        self.assertEqual(actual_output[0], "It's freezing!", f"Got {actual_output[0]}, expected 'It\'s freezing!'")

    def test_exercise_b2(self):
        from exercises.exercise_b import check_speed_limit

        # Capture output of print statement.
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call function.
        check_speed_limit()

        # Restore original stdout.
        sys.stdout = sys.__stdout__

        # Check output.
        actual_output = captured_output.getvalue().strip().splitlines()
        self.assertEqual(len(actual_output), 1, f"Required 1 print statement, received {len(actual_output)}")
        self.assertEqual(actual_output[0], 'Slow down!', f"Got {actual_output[0]}, expected 'Slow down!'")

    def test_exercise_b3(self):
        from exercises.exercise_b import check_balance

        # Capture output of print statement.
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call function.
        check_balance()

        # Restore original stdout.
        sys.stdout = sys.__stdout__

        # Check output.
        actual_output = captured_output.getvalue().strip().splitlines()
        self.assertEqual(len(actual_output), 1, f"Required 1 print statement, received {len(actual_output)}")
        self.assertEqual(actual_output[0], 'Low balance: $10.5', f"Got {actual_output[0]}, expected 'Low balance: $10.5'")

    def test_exercise_b4(self):
        from exercises.exercise_b import check_age

        # Capture output of print statement.
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call function.
        check_age()

        # Restore original stdout.
        sys.stdout = sys.__stdout__

        # Check output.
        actual_output = captured_output.getvalue().strip().splitlines()
        self.assertEqual(len(actual_output), 1, f"Required 1 print statement, received {len(actual_output)}")
        self.assertEqual(actual_output[0], 'Age check complete', f"Got {actual_output[0]}, expected 'Age check complete'")

if __name__ == '__main__':
    unittest.main()

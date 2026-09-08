import unittest
from io import StringIO
import sys
from unittest import mock

class UserInputTestCase(unittest.TestCase):
    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_console_output_with_input(self):
        with mock.patch('builtins.input', return_value="Indian food, korean food, and most foods"):
            exec(open('user_input_exercise.py').read())

        output = self.captured_output.getvalue().strip()

        EXPECTED = "Your favorite food is: Indian food, korean food, and most foods"
        self.assertEqual(output, EXPECTED)

if __name__ == '__main__':
    unittest.main()
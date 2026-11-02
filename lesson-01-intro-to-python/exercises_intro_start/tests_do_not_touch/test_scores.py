import unittest
from io import StringIO
import sys
from unittest import mock

class ScoresTestCase(unittest.TestCase):
    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_console_output_with_input(self):
        with mock.patch('builtins.input', side_effect=[10, 20, 30]):
            exec(open('scores.py').read())

        output = self.captured_output.getvalue().strip().split("\n")
        output.sort()

        expected_items = [
            'Test Score 1: 10.0',
            'Test Score 2: 20.0',
            'Test Score 3: 30.0',
            'Average Score: 20.0'
        ]
        expected_items.sort()
        self.assertListEqual(output, expected_items)

if __name__ == '__main__':
    unittest.main()
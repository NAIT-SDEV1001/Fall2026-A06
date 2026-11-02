import unittest
from io import StringIO
import sys
from unittest import mock

class CookieTestCase(unittest.TestCase):
    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_console_output_with_input(self):
        with mock.patch('builtins.input', return_value="25"):
            exec(open('cookies.py').read())

        output = self.captured_output.getvalue().strip()

        EXPECTED = "You ate 25 cookies\nWhich is equal to: 1875.0 calories"
        self.assertEqual(output, EXPECTED)

if __name__ == '__main__':
    unittest.main()
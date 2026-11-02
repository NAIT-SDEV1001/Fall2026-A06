import unittest
from io import StringIO
import sys

class FixMeTestCase(unittest.TestCase):
    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_console_output(self):
        exec(open('fix_me.py').read())

        output = self.captured_output.getvalue().strip()

        EXPECTED = 'hi there\nmy name is \nThe computer running this code'
        self.assertEqual(output, EXPECTED)

if __name__ == '__main__':
    unittest.main()
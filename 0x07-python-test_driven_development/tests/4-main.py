
import unittest
from io import StringIO
import sys

module_name = "4-print_square"
print_square = __import__('4-print_square').print_square

class TestPrintSquare(unittest.TestCase):
    def setUp(self):

        self.saved_stdout = sys.stdout
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = self.saved_stdout

    def test_print_square_4(self):
        expected_output = "####\n" \
                          "#  #\n" \
                          "#  #\n" \
                          "####\n"
        print_square(4)
        self.assertEqual(self.output.getvalue(), expected_output)

    def test_print_square_10(self):
        expected_output = "##########\n" \
                          "#        #\n" \
                          "#        #\n" \
                          "#        #\n" \
                          "#        #\n" \
                          "#        #\n" \
                          "#        #\n" \
                          "#        #\n" \
                          "#        #\n" \
                          "##########\n"
        print_square(10)
        self.assertEqual(self.output.getvalue(), expected_output)

    def test_print_square_0(self):
        expected_output = ""
        print_square(0)
        self.assertEqual(self.output.getvalue(), expected_output)

    def test_print_square_1(self):
        expected_output = "#\n"
        print_square(1)
        self.assertEqual(self.output.getvalue(), expected_output)

    def test_print_square_negative(self):
      
        with self.assertRaises(Exception) as context:
            print_square(-1)
        self.assertTrue("size must be >= 0" in str(context.exception))

if __name__ == '__main__':
    unittest.main()

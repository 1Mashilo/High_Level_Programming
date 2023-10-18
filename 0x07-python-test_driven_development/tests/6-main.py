
import unittest 

module_name = "6-max_integer"
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer_with_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result, "Expected None for an empty list")

    def test_max_integer_with_single_element(self):
        result = max_integer([42])
        self.assertEqual(result, 42, "Expected the only element to be the maximum")

    def test_max_integer_with_multiple_elements(self):
        result = max_integer([10, 5, 20, 15])
        self.assertEqual(result, 20, "Expected 20 to be the maximum")

    def test_max_integer_with_negative_numbers(self):
        result = max_integer([-5, -10, -1, -3])
        self.assertEqual(result, -1, "Expected -1 to be the maximum")

    def test_max_integer_with_mixed_numbers(self):
        result = max_integer([5, -10, 0, 42, -3])
        self.assertEqual(result, 42, "Expected 42 to be the maximum")

if __name__ == '__main__':
    unittest.main()

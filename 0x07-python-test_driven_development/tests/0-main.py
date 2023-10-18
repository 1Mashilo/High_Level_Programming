
module_name = "0-add_integer"
add_integer = __import__(module_name).add_integer

import unittest


class TestAddInteger(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        result = add_integer(1, 2)
        self.assertEqual(result, 3)
    
    def test_add_mixed_types(self):
        result = add_integer(100.5, 2)
        self.assertEqual(result, 102)
    
    def test_add_invalid_input(self):
        with self.assertRaises(TypeError):
            add_integer("Hello", 2)
            add_integer(4, None)

if __name__ == '__main__':
    unittest.main()

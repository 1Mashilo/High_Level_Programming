

import unittest
module_name = "3-say_my_name"
say_my_name = __import__(module_name).say_my_name

class TestSayMyName(unittest.TestCase):

    def test_say_my_name_valid_input(self):
        result = say_my_name("John", "Smith.")
        self.assertEqual(result, "My name is John Smith.")

    def test_say_my_name_missing_last_name(self):
        with self.assertRaises(TypeError):
            say_my_name("Walter")

    def test_say_my_name_invalid_input(self):
        with self.assertRaises(TypeError):
            say_my_name(12, "White")

if __name__ == "__main__":
    unittest.main()

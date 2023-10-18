
import unittest

module_name = "2-matrix_divided"
matrix_divided = __import__(module_name).matrix_divided

class TestMatrixDivided(unittest.TestCase):
    def test_divide_integer_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        divisor = 2
        result = matrix_divided(matrix, divisor)
        expected_result = [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]
        self.assertEqual(result, expected_result)

    def test_divide_float_matrix(self):
        matrix = [[1.0, 2.5, 3.6], [4.8, 5.2, 6.0]]
        divisor = 2
        result = matrix_divided(matrix, divisor)
        expected_result = [[0.5, 1.25, 1.8], [2.4, 2.6, 3.0]]
        self.assertEqual(result, expected_result)

    def test_divide_integer_matrix_with_float_divisor(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        divisor = 2.5
        result = matrix_divided(matrix, divisor)
        expected_result = [[0.4, 0.8, 1.2], [1.6, 2.0, 2.4]]
        self.assertEqual(result, expected_result)

    def test_divide_matrix_by_zero(self):
        matrix = [[1, 2], [3, 4]]
        divisor = 0
        with self.assertRaises(ZeroDivisionError):
            matrix_divided(matrix, divisor)

    def test_invalid_matrix_type(self):
        matrix = "not_a_matrix"
        divisor = 2
        with self.assertRaises(TypeError):
            matrix_divided(matrix, divisor)

    def test_matrix_with_different_row_lengths(self):
        matrix = [[1, 2, 3], [4, 5]]
        divisor = 2
        with self.assertRaises(TypeError):
            matrix_divided(matrix, divisor)

    def test_invalid_divisor_type(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        divisor = "not_a_number"
        with self.assertRaises(TypeError):
            matrix_divided(matrix, divisor)

if __name__ == "__main__":
    unittest.main()

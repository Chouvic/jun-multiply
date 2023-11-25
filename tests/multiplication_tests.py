import unittest
from jun_multiply import Multiplication


class MultiplicationTestCase(unittest.TestCase):

    def setUp(self):
        self.multiplication = Multiplication(2)

    def test_zero(self):
        """Test 0 multiplied by 2"""
        result = self.multiplication.multiply(0)
        self.assertEqual(result, 0)

    def test_natural_number(self):
        """Test natural number 5 multiplied by 2"""
        result = self.multiplication.multiply(5)
        self.assertEqual(result, 10)

    def test_integer_number(self):
        """Test integer number -7 multiplied by 2"""
        result = self.multiplication.multiply(-7)
        self.assertEqual(result, -14)


if __name__ == "__main__":
    unittest.main()

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        """Test addition operation."""
        result = self.calc.add(2, 4)
        self.assertEqual(result, 6)

    def test_subtraction(self):
        """Test subtraction operation."""
        result = self.calc.subtract(10, 8)
        self.assertEqual(result, 2)

    def test_multiplication(self):
        """Test multiplication operation."""
        result = self.calc.multiply(3, 3)
        self.assertEqual(result, 9)

    def test_division(self):
        """Test division operation."""
        result = self.calc.divide(10, 10)
        self.assertEqual(result, 1)

    def test_division_by_zero(self):
        """Test division by zero."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()

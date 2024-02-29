import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        """Test addition operation."""
        self.assertEqual(self.calc.add(4, 4), 8)

    def test_subtraction(self):
        """Test subtraction operation."""
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_multiplication(self):
        """Test multiplication operation."""
        self.assertEqual(self.calc.multiply(5, 2), 10)

    def test_division(self):
        """Test division operation."""
        self.assertEqual(self.calc.divide(10, 10), 1)

    def test_division_by_zero(self):
        """Test division by zero."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()

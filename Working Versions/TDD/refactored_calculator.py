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

    def test_power(self):
        self.assertEqual(self.calc.power(2,3), 8)  # 2^3 = 8
        self.assertEqual(self.calc.power(3,2), 9)  # 3^2 = 9
        

    def test_factorial(self):
        self.assertEqual(self.calc.factorial(0), 1)  # 0! = 1
        self.assertEqual(self.calc.factorial(1), 1)  # 1! = 1
        self.assertEqual(self.calc.factorial(5), 120)  # 5! = 5 * 4 * 3 * 2 * 1 = 120

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)

if __name__ == '__main__':
    unittest.main()
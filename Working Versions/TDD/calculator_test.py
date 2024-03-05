import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        calc = Calculator()
        result = calc.add(2, 4)
        self.assertEqual(result, 6)


    def test_subtraction(self):
        calc = Calculator()
        result = calc.subtract(10, 8)
        self.assertEqual(result, 2)


    def test_multiplication(self):
        calc = Calculator()
        result = calc.multiply(3, 3)
        self.assertEqual(result,9)


    def test_division(self):
        calc = Calculator()
        result = calc.divide(10, 10)
        self.assertEqual(result, 1)


    def test_division_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

    def test_power(self):
        calc = Calculator()
        result = calc.power(2, 3)
        self.assertEqual(result, 8)  # 2^3 = 8

    def test_factorial(self):
        calc = Calculator()
        result = calc.factorial(5)
        self.assertEqual(result, 120)  # 5! = 120

    def test_factorial_negative(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.factorial(-1)


if __name__ == '__main__':
    unittest.main()
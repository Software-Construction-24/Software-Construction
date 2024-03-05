class Calculator:
    def add(self, x, y):
        return x + y


    def subtract(self, x, y):
        return x - y


    def multiply(self, x, y):
        return x * y


    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
    
    def power(self, x, y):
        """Exponential function"""
        return x ** y

    def factorial(self, n):
        """Factorial function"""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
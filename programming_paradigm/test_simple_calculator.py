import unittest
from simple_calculator import SimpleCalculator 
# Assuming simple_calculator.py is in the same directory.

class TestSimpleCalculator(unittest.TestCase):
    """
    Unit tests for the SimpleCalculator class, ensuring compliance with 
    specific naming conventions for test methods.
    """

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # -----------------
    # Test Cases for add() - Combined into the required test_addition method
    # -----------------
    def test_addition(self):
        """Test the add method with various scenarios (positive, negative, zero, floats)."""
        # Two positive numbers
        self.assertEqual(self.calc.add(5, 3), 8)
        # Two negative numbers
        self.assertEqual(self.calc.add(-5, -3), -8)
        # Mixed signs
        self.assertEqual(self.calc.add(-5, 3), -2)
        self.assertEqual(self.calc.add(5, -3), 2)
        # With zero
        self.assertEqual(self.calc.add(0, 5), 5)
        # Floating point numbers (using assertAlmostEqual for safety, though equal should work here)
        self.assertAlmostEqual(self.calc.add(1.5, 2.5), 4.0)

    # -----------------
    # Test Cases for subtract()
    # -----------------
    def test_subtraction(self):
        """Test the subtract method with various scenarios."""
        # Positive result
        self.assertEqual(self.calc.subtract(10, 4), 6)
        # Negative result
        self.assertEqual(self.calc.subtract(4, 10), -6)
        # Subtracting a negative number (a - (-b) = a + b)
        self.assertEqual(self.calc.subtract(5, -3), 8)
        # Subtracting zero
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # -----------------
    # Test Cases for multiply()
    # -----------------
    def test_multiplication(self):
        """Test the multiply method with various scenarios."""
        # Two positive
        self.assertEqual(self.calc.multiply(5, 4), 20)
        # Mixed signs
        self.assertEqual(self.calc.multiply(5, -4), -20)
        # Two negative
        self.assertEqual(self.calc.multiply(-5, -4), 20)
        # Multiplication by zero (Edge Case)
        self.assertEqual(self.calc.multiply(100, 0), 0)

    # -----------------
    # Test Cases for divide() - Includes Division by Zero Edge Case
    # -----------------
    def test_division(self):
        """Test the divide method with various scenarios, including the zero-division edge case."""
        # Normal division (integer result)
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        # Normal division (float result)
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.3333333333333335)
        # Division with negative numbers
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        # Division of zero (0 / x)
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        
        # Critical Edge Case: Division by Zero
        # Verifies that the method correctly returns None as implemented in SimpleCalculator.
        self.assertIsNone(self.calc.divide(10, 0))

if __name__ == '__main__':
    unittest.main()
import unittest
# Import the SimpleCalculator class from the provided script
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class methods.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method runs.
        """
        self.calc = SimpleCalculator()

    # --- Tests for the add method ---

    def test_addition_positive_integers(self):
        """Test addition with two positive integers."""
        self.assertEqual(self.calc.add(5, 7), 12)

    def test_addition_negative_integers(self):
        """Test addition with two negative integers."""
        self.assertEqual(self.calc.add(-5, -7), -12)

    def test_addition_mixed_integers(self):
        """Test addition with a positive and a negative integer."""
        self.assertEqual(self.calc.add(10, -3), 7)
        self.assertEqual(self.calc.add(-8, 5), -3)

    def test_addition_floats(self):
        """Test addition with floating-point numbers."""
        self.assertAlmostEqual(self.calc.add(1.5, 2.5), 4.0)

    def test_addition_with_zero(self):
        """Test addition when one operand is zero."""
        self.assertEqual(self.calc.add(5, 0), 5)

    # --- Tests for the subtract method ---

    def test_subtraction_positive_integers(self):
        """Test subtraction where the result is positive."""
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_subtraction_negative_result(self):
        """Test subtraction where the result is negative."""
        self.assertEqual(self.calc.subtract(3, 10), -7)

    def test_subtraction_negative_operands(self):
        """Test subtraction with negative operands."""
        self.assertEqual(self.calc.subtract(-5, -2), -3) # -5 - (-2) = -3
        self.assertEqual(self.calc.subtract(5, -2), 7)   # 5 - (-2) = 7

    def test_subtraction_floats(self):
        """Test subtraction with floating-point numbers."""
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.5), 3.0)

    # --- Tests for the multiply method ---

    def test_multiplication_positive_integers(self):
        """Test multiplication of two positive integers."""
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiplication_negative_result(self):
        """Test multiplication of a positive and a negative integer."""
        self.assertEqual(self.calc.multiply(4, -3), -12)
        self.assertEqual(self.calc.multiply(-4, 3), -12)

    def test_multiplication_two_negatives(self):
        """Test multiplication of two negative integers."""
        self.assertEqual(self.calc.multiply(-4, -3), 12)

    def test_multiplication_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(self.calc.multiply(100, 0), 0)

    def test_multiplication_floats(self):
        """Test multiplication with floating-point numbers."""
        self.assertAlmostEqual(self.calc.multiply(2.5, 2.0), 5.0)

    # --- Tests for the divide method ---

    def test_division_positive_result(self):
        """Test division resulting in a positive number."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)

    def test_division_negative_result(self):
        """Test division resulting in a negative number."""
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, 2), -5.0)

    def test_division_two_negatives(self):
        """Test division of two negative numbers (positive result)."""
        self.assertEqual(self.calc.divide(-10, -2), 5.0)

    def test_division_float_result(self):
        """Test division resulting in a non-integer float."""
        self.assertEqual(self.calc.divide(10, 4), 2.5)

    def test_division
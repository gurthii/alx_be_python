def safe_divide(numerator, denominator):
    """
    Performs division of two values, robustly handling ZeroDivisionError
    and ValueError (for non-numeric inputs).

    Args:
        numerator (str or number): The dividend.
        denominator (str or number): The divisor.

    Returns:
        str: A string containing the result or an appropriate error message.
    """
    try:
        # Attempt to convert both inputs to float
        num = float(numerator)
        den = float(denominator)

        # Attempt the division
        result = num / den

        # Return the successful result
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # Catch error if the denominator is 0
        return "Error: Cannot divide by zero."

    except ValueError:
        # Catch error if either input cannot be converted to a float (non-numeric)
        return "Error: Please enter numeric values only."

# Optional: Example usage for internal testing
if __name__ == "__main__":
    print(f"10 / 5: {safe_divide('10', '5')}")
    print(f"10 / 0: {safe_divide('10', '0')}")
    print(f"ten / 5: {safe_divide('ten', '5')}")
    print(f"10 / five: {safe_divide('10', 'five')}")
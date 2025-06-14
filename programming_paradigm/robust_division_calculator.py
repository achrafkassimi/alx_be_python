# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Perform division and handle errors such as division by zero and non-numeric input."""
    try:
        # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."
    
    try:
        # Attempt to perform division
        result = numerator / denominator
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."
    
    # If no errors, return the result of the division
    return f"The result of the division is {result}"


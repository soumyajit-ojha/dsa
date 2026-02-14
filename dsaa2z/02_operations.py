# 1. Implicit Type Conversion
# This is automatic. Python converts a smaller data type to a larger data type to prevent data loss.
# The Logic: If you perform an operation between an integer and a float, Python "promotes" the integer to a float because floats can hold more information (decimals).
# Example: 5 + 2.0 = 7.0 (Here, 5 (int) is implicitly converted to $5.0$ (float).)

# 2. Explicit Type Conversion
# This is manual. You use built-in functions to force a value into a specific type.
# This is required when Python cannot guess your intent (like turning the string "10" into a number).

# Common Functions:
# int(): Converts to integer (truncates decimals).
# float(): Converts to decimal number.
# str(): Converts any value into a string.
# list(), tuple(), set(): Converts collections.

"""
NOTE:
You cannot explicitly convert a string to an integer if the string contains non-numeric characters (e.g., int("apple") will cause a ValueError).
"""

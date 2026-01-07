# An integer d is a divisor of an integer v if the remainder of n % d = 0 .

# Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.

# Example
# n = 124
# Check whether 1, 2 and 4 are divisors of 124. All 3 numbers divide evenly into  so return 3.

# n = 111
# Check whether 1, 1, and 1 are divisors of 111. All 3 numbers divide evenly into 111 so return 3.

# n = 10
# Check whether 1 and 0 are divisors of 10. 1 is, but 0 is not. Return 1.

# Function Description

# Complete the findDigits function in the editor below.
#   findDigits has the following parameter(s):
#   int n: the value to analyze
# Returns
#   int: the number of digits in  that are divisors of


def find_digits(n: int) -> int:
    num_str = str(n)
    try:
        for i in num_str:
            if n % int(i) == 0:
                continue
            else:
                return 1
        return 3
    except ZeroDivisionError:
        return 1

# findDigits = lambda n: sum(1 for d in str(n) if int(d) != 0 and n % int(d) == 0)
res = find_digits(1110)
print(res)

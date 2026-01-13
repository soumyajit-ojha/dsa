# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

# for loo

# for i in range(1, num):
#     if i*i <= num and i > res:
#         res = i
# print(res)

# binary-search (while loop)


def sqrt_num(x: int) -> int:
    left = 0
    right = x
    res = 0
    while left <= right:
        mid = (left + right) // 2
        if (mid * mid) <= x:
            res = mid
            left = mid + 1
        elif (mid * mid) >= x:
            right = mid - 1
    return res


s = sqrt_num(16)
print(s)

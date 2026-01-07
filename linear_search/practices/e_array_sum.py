# Given an array of integers, find the sum of its elements.
# For example, if the array ar = [1, 2, 3], 1+2+3 = 6 , so return 6.
# Function Description
# Complete the simple_array_sum function with the following parameter(s):
# ar[n]: an array of integers
# Returns
# : the sum of the array elements


def simple_array_sum(arr: list) -> int:
    res = 0
    for i in arr:
        res += i
    return res


ar = [1, 2, 3, 4, -1, -2]
res = simple_array_sum(arr=ar)
print(res)

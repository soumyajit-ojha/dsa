# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.


# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# SUDO-CODE:
#   array = [1, 2, 3, 4]
#   target = 3
#   left_point = 0
#   right_point = len(array) + 1
#   while loop (left <= right):
#       mid_point = (left+right) // 2       # return an integer
#       if target value == mid index value:
#           return mid index
#       if target value < mid index value:
#           right_point = mid point + 1
#       else :
#           left_point = mid_= point + 1

from typing import List


def search_target_index(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return None


ar = [-1, 0, 3, 5, 9, 12]
tar = 1
print(search_target_index(arr=ar, target=tar))

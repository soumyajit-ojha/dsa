#  search a number from  a sorted array.
# data = [2, 5, 7, 10, 19]
# tar = 7

# process
# step 1: create two point left and right (choose the index value).
# step 2: start the iteration.
# step 3: find the mid point. and compare to tagate either the target is greater or leess than mid point.
# step 4: if targer is lesser change the value right point to mid, if target is greater change lower value to mid.
# start checking untill get the result or the iteration complited.

l = [2, 5, 7, 10, 19]
t = 7

left = 0
right = len(l) - 1

while left < right:
    mid = (left + right) // 2  # floor division give the middle value.
    if l[mid] == t:
        print(f"the index of the {t} is {mid}")
        break
    elif t < mid:
        right = mid
    else:
        left = mid


# Get the first occurance of target in a sorted array.
# list = [1,2,2,2,3,4] target = 2 → return 3
# PROCEDURE:
# 1. take two variable left and right with minimum and maximum index of given list.
# 2. take another variable to keep record of last occurance's index.
# 3. start iteration and find the mid value,
# 4. check condition that either the mid value is greater or lesser than target.
#   if target < mid: -> right = mid
#   if target > mid: -> left = mid

lst = [1, 2, 2, 2, 3, 4]
tar = 2
first_ocr = None

while left <= right:
    mid = (left + right) // 2

    if lst[mid] == tar:
        first_ocr = mid
        right = mid - 1
    elif lst[mid] < tar:
        left = mid + 1
    else:
        right = mid - 1

# print(first_ocr)


def findMin(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1
    ans = float("inf")
    print("Initial ANS", ans)
    while left <= right:
        mid = (left + right) // 2
        print("Mid value", mid)
        if nums[mid] < nums[left]:
            ans = min(ans, nums[mid])
            right = mid - 1
            print("Answer", ans)
        else:
            ans = min(ans, nums[left])
            left = mid + 1
            print("Answer", ans)
    return ans


print(findMin(nums=[3, 4, 5, 1, 2]))

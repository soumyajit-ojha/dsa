# Merge sort

"""
1. its a recursive algorithm
2. create a function take 3 args (arr, start index, end index)
    eg. merge_sort(arr, s, e)

3. find the mid of the arr.
4. sort the left half by calling merge_sort assign to a var "left".
    eg. merge_sort(arr, start, mid)

5. sort the right half by calling merge_sort and assign to a var "right".
    eg. merge_sort(arr, mid+1, end)

6. now compare both left and right which one is smaller and replace this value to main array index.
   gradually increace the index of left and right, compare them and keep the lower value to main array.
   complete the process untill the array sorted.
"""


# def merge_sort(arr: list, s: int, e: int) -> list:
#     if s == e:
#         return [arr[s]]
#     mid = (s + e) // 2
#     left = merge_sort(arr, s, mid)
#     right = merge_sort(arr, mid + 1, e)

#     # k = 0 "its used for main array which should be hardcoded."
#     i, j, k = 0, 0, s
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             arr[k] = left[i]
#             i += 1
#         else:
#             arr[k] = right[j]
#             j += 1
#         k += 1
#     while i <len(left):
#         arr[k] = left[i]
#         i+=1
#         k+=1
#     while j < len(right):
#         arr[k] = left[j]
#         j+=1
#         k+=1
#     return arr[s: e+1]


def merge_sort(arr: list, s: int, e: int) -> list:
    # 1. Base Case: If the segment has only one element, return it as a list
    if s == e:
        return [arr[s]]

    mid = (s + e) // 2

    # 2. Divide: Recursively split and get the sorted halves
    left = merge_sort(arr, s, mid)
    right = merge_sort(arr, mid + 1, e)

    # 3. Conquer (Merge): Combine 'left' and 'right' back into 'arr'
    i, j, k = 0, 0, s
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # 4. Cleanup: Copy any remaining elements
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    # 5. Return the sorted segment for the next level of recursion
    return arr[s : e + 1]


a = [3, 2, 5, 8, 6]

res = merge_sort(a, 0, 4)
print(res)

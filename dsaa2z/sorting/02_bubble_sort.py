# Bubble sort.


def bubble_sort(arr: list):
    n = len(arr)
    for i in range(n):  #   0 1 2 3 4
        is_sorted = False
        for j in range(n - 1 - i):  # 0 1 2 3
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                is_sorted = True
        if is_sorted:
            break
        print(arr)
    return arr


arr = [105, 3, 15, 11, 65]
res = bubble_sort(arr=arr)
print(res)


"""
NOTE: 
The Intended Flow
The goal of this program is to sort the array by comparing neighbors. If a number is larger than its neighbor to the right, they swap. Large numbers "bubble" to the end.

Step-by-Step Logic
Outer Loop (i): This runs the "passes." After each pass, the largest remaining number is guaranteed to be at the end of the list.

Inner Loop (j): This iterates through the unsorted portion of the list (n-1-i).

Comparison: It checks if the current element arr[j] is greater than its neighbor arr[j+1].

If True: It swaps them.

If False: It triggers the else block.

The Flag (is_sorted): This is intended to stop the program early if the list is already sorted.
"""

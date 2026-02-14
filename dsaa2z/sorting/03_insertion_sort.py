# Insertion sort


def insertion_sort(arr: list):
    n = len(arr)
    for i in range(1, n):
        # print("Loop for I = ", i)
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            # print(arr[j - 1], arr[j])
            # print("before", arr)
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            # print("after", arr)
            j -= 1
    return arr


a = [4, 3, 2, 1]
res = insertion_sort(arr=a)
print(res)


"""
NOTE: 

Gemini said
The program you wrote is a classic Insertion Sort. It works by treating the left side of the list as a "sorted zone" and moving into it one element at a time from the right.

Simple Flow of the Program
Start at the Second Element: The outer loop (for i in range(1, n)) starts at index 1. It assumes the very first element (index 0) is already "sorted" because a single number can't be out of order.

Pick a "Guest": The variable j = i keeps track of the element we are currently trying to place into the sorted zone.

The Backward Comparison: The while loop looks to the left (arr[j - 1]). It asks: "Is the number on my left bigger than me?"

The Step-Back (Swap): If the neighbor on the left is bigger, they swap places. This moves our "guest" one step toward the beginning of the list.

Repeat: The j -= 1 ensures we keep comparing our element with the next neighbor to the left until:

It finds a neighbor that is smaller (meaning it's in the right spot).

It reaches the very start of the list (j > 0 becomes false).

Build the Wall: Once the while loop finishes, that element is settled, and the outer loop moves to the next i to repeat the process.

Visualizing the a = [4, 3, 2, 1] Flow
Pass 1 (i=1): 3 is compared with 4. Since 3<4, they swap.

List: [3, 4, 2, 1]

Pass 2 (i=2): 2 is compared with 4 (swap) then with 3 (swap).

List: [2, 3, 4, 1]

Pass 3 (i=3): 1 is compared with 4 (swap), then 3 (swap), then 2 (swap).

List: [1, 2, 3, 4]

"""

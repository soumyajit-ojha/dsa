# Selection sort.

arr = [105, 3, 4, 11, 65]


n = len(arr)
for i in range(n):
    f_index = i
    print("F index before:", f_index)
    for j in range(i + 1, n):
        if arr[f_index] > arr[j]:
            f_index = j
        print("F index after:", f_index)
    arr[i], arr[f_index] = arr[f_index], arr[i]
    print("Switched")


print(arr)


"""
NOTE:

Simple Flow of the Program
Outer Loop (i): This loop keeps track of the "frontier." Everything to the left of i is already sorted. It moves from the first element to the last.

Setting the Initial Minimum (f_index): At the start of each pass, we assume the first unsorted element (at index i) is the smallest. we store its position in f_index.

The Search (Inner Loop j): This loop looks at every other element to the right of i.

It asks: "Is there any number smaller than what I have at f_index?"

If it finds a smaller number, it updates f_index to that new position.

The Swap: After the inner loop finishes, f_index now points to the actual smallest number in the unsorted part.

We swap the value at arr[i] with the value at arr[f_index].

Repeat: The "sorted" boundary moves one step to the right, and the process repeats until the entire list is organized.

Visualizing the arr = [105, 3, 4, 11, 65] Flow
Pass 1 (i=0):

f_index starts at 0 (value 105).

The inner loop finds 3 is the smallest. f_index becomes 1.

Swap 105 and 3.

Array: [3, 105, 4, 11, 65]

Pass 2 (i=1):

f_index starts at 1 (value 105).

The inner loop finds 4 is the smallest. f_index becomes 2.

Swap 105 and 4.

Array: [3, 4, 105, 11, 65]

Pass 3 (i=2):

f_index starts at 2 (value 105).

The inner loop finds 11 is the smallest. f_index becomes 3.

Swap 105 and 11.

Array: [3, 4, 11, 105, 65]

Pass 4 (i=3):

f_index starts at 3 (value 105).

The inner loop finds 65 is the smallest. f_index becomes 4.

Swap 105 and 65.

Array: [3, 4, 11, 65, 105]
"""

Here is a comprehensive guide to **Linear Search**, covering everything from the basics to practice problems.

---

### 1. What is Linear Search?
**Linear Search** (also known as Sequential Search) is the simplest searching algorithm. It works by checking every element in a list one by one, from the beginning to the end, until the desired element (target) is found or the list ends.

**The Analogy:**
Imagine looking for a specific book on a messy, unorganized shelf. You have to pick up the first book, check the title, put it back, pick up the second book, check the title, and so on, until you find the book you want.

---

### 2. Why Linear Search?
Even though there are faster algorithms (like Binary Search), Linear Search is still widely used because:

1.  **Simplicity:** It is very easy to understand and implement.
2.  **No Sorting Required:** Unlike Binary Search, Linear Search works on **unsorted** arrays.
3.  **Memory Efficient:** It does not require any extra memory space (Space Complexity is $O(1)$).
4.  **Streaming Data:** If data is arriving one by one and not stored in a structure yet, you have to check it linearly.
5.  **Small Datasets:** For very small lists (e.g., < 100 elements), the difference in speed between Linear Search and complex algorithms is negligible.

---

### 3. What are the prerequisites?
To implement Linear Search, you only need:
1.  **A Collection:** An array, list, or linked list containing data.
2.  **Traversal Mechanism:** A way to visit elements one by one (a `for` loop or `while` loop).
3.  **Comparison Logic:** A way to compare the current element with the target value (e.g., `if A == B`).

*Note: The data does **not** need to be sorted.*

---

### 4. How to implement Linear Search?
Here is the implementation in Python (logic applies to Java/C++ as well).

**Algorithm:**
1. Start from index 0.
2. Compare the current element with the target.
3. If they match, return the index.
4. If they don't match, move to the next index.
5. If you reach the end of the list without finding the target, return -1 (indicating not found).

**Code (Python):**
```python
def linear_search(arr, target):
    # Iterate through the range of the array length
    for i in range(len(arr)):
        # Check if current element equals target
        if arr[i] == target:
            return i  # Return the index if found
            
    return -1  # Return -1 if target is not in the list

# Example Usage
numbers = [10, 50, 30, 70, 80, 20]
key = 30

result = linear_search(numbers, key)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")
```

---

### 5. Where do I need to use Linear Search?
You should use it when:
*   The list is **unsorted**.
*   The list is **small**.
*   You are using a **Linked List** (since you cannot randomly access the middle element like in Binary Search).
*   You are doing a "one-off" search (sorting a list takes longer than just scanning it once).

---

### 6. Time Complexity (Best and Worst Case)

*   **Best Case:** $O(1)$
    *   **Scenario:** The target element is at the **very first index** (index 0). The loop runs only once.
*   **Worst Case:** $O(N)$
    *   **Scenario:** The target element is at the **very last index** or **not present** at all. The algorithm has to check all $N$ elements.
*   **Average Case:** $O(N)$

---

### 7. Practice Questions (LeetCode / HackerRank)

Since Linear Search is simple, "Hard" problems usually involve using a Linear Scan ($O(N)$ approach) to solve a complex problem efficiently, rather than just "finding a number."

#### **Level: Easy (Basic Implementation)**
1.  **Linear Search** (HackerRank) - *The standard implementation.*
2.  **Find Numbers with Even Number of Digits** (LeetCode 1295) - *Traverse array and count digits.*
3.  **Max Consecutive Ones** (LeetCode 485) - *Scan the array to find the longest sequence of 1s.*
4.  **Find the Index of the First Occurrence in a String** (LeetCode 28) - *Linear scan of a string.*

#### **Level: Medium (Logic based on Linear Scan)**
5.  **Best Time to Buy and Sell Stock** (LeetCode 121) - *Find min price and max profit in a single pass (Linear Scan).*
6.  **Product of Array Except Self** (LeetCode 238) - *Uses two linear passes (forward and backward) to solve without division.*
7.  **Find the Duplicate Number** (LeetCode 287) - *Can be solved with linear scan using a frequency array or hash map.*
8.  **Majority Element** (LeetCode 169) - *Moore’s Voting Algorithm (A smart linear scan).*

#### **Level: Hard (Optimizing to O(N) using Linear Scan)**
*Note: These are hard because coming up with the $O(N)$ solution is difficult, not because the code is long.*

9.  **First Missing Positive** (LeetCode 41) - *Uses a linear scan to place numbers in correct positions, then another scan to find the missing one.*
10. **Trapping Rain Water** (LeetCode 42) - *Can be solved using a two-pointer approach, which is essentially a linear scan from both ends meeting in the middle.*
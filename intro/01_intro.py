# Data Structure and algorithm.

"""
Data: the raw information
Structure: the storage where we keep the data.
    - linear data structure
        - Array
        - Linked List
        - Stack
        - Queue
    - non-linear data structure
        - Tree
        - graph

algorithm: the sets of information to solve the problem


Time complexity: This is the consumed by program according to the input size.
    - Its denoted by big O notation.
    - time complexity comparision.
        O-1 < O-log-log-n < O-log-n < O-n < O-n^2 < O-n^3 < ..... < On^n < O-2^n
        NOTE: n is the input size

    - As like mathematical equations.
    1. linear -> 2x + 3 => highest factor = x
    2. Quadratic -> 2x^2 + 3X + 3 => highest factor = x^2
    3. cubic -> 4x^3 + 2x^2 + 3X + 3 => highest factor = x^3
    4. logarthmic -> log x + 5 => highest factor = log x
    5. exponential -> 3^x + 10 => highest factor = 3^x

    [As like mathematical equation to find higher degree of equation, we check the time complexity.]

Type of Analysis:
    1. Best Case (min time) - denoted by omega (Ω)
    2. Avg Case (Average Case) - demoted by theta (θ)
    3. Wrost case (max time) - denoted by big O (O)
"""
# Time Complexity:
"""
CONSTANT TIME: 
    - Denoted by O(1)
    - Here the program executed only once and its constant for small or big inputs.
    -eg. even odd checker.
"""
n1 = 1000
n2 = 23
value = n1 * n2
if value % 2 == 0:
    print("Even")
else:
    print("Odd")

"""
LINEAR TIME
    - Denoted by O(n)
    - here the program execution time depends on the input size. It increase or decrease on input size.
    - if in program there is loop is used (not nested), one or more independent.
    - eg. printing number in a range.
"""

n = 10
for i in range(10):
    print(i+1)




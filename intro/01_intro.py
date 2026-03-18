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
LINEAR TIME:
    - Denoted by O(n)
    - here the program execution time depends on the input size. It increase or decrease on input size.
    - if in program there is loop is used (not nested), one or more independent.
    - eg. printing number in a range.
"""

n = 10
for i in range(10):
    print(i + 1)

for i in range(n):
    print(n * n)

# for above 2 program time complexity is O(n).

"""
Quadratic Time:
    - Denoted by O(n^2):
    - The excution time of the program depends on time which is n * n (n is the input size.)
    - In this type of program there is nested loops.
    - bubble sort algorithm.
"""

n = 5
for i in range(n):
    for j in range(n):
        print(j)  # time complexity of this program is o(n^2)


"""
Cubic Time:
    - Denoted by O(n^3):
    - The excution time of the program depends on time which is n * n * n(n is the input size.)
    - In this type of program there is nested loops.
"""

n = 5
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(j)  # time complexity of this program is o(n^2)

"""
Logarithmic Time Complexity:
    - Denoted by O(log n)
    - In this time complexity the program execute log n times.
    - As long as program move ahead its no of excecution reduces.
    - binary search algorithm.
"""

n = 10
while n > 0:
    print(n)
    n = n // 2
"""
initial (n) ||  print(value)  || calculate (n)
n = 10          10                  n = 5
n = 10          5                   n = 2
n = 2           2                   n = 1

the value of n reduce by the form of if the no of loop is k times.
n -> n/2^1 -> n/2^2 -> n/2^3 -> n/2^4 ..... n/2^k

- At last the n/2^k = 1
=> n/2^k = 1
=> n = 2^k
=> log n = log 2^k
=> log n = k log 2
=> (log n) / (log 2) = k ::: log 2 = constant value -> must ignored in time complexity
=> k = log n
"""

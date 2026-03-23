"""
By using numpy we can create multi-Dimensional array.
"""

import numpy as np

# 1. Create a 0-Dimensional array.
"""
Zero D array  has only single element.
Its just a point.
"""

zero_d_arr = np.array([1])
print("Zero D array \n", zero_d_arr)

# 2. 1 - Dimensional Array.
"""
One  D array is the collection of 0-D array.
move in straight line, (eiter row or column)
"""
one_d_array = np.array([1, 2, 3, 10, 20, 30, 100, 200, 300])
print("One Dimensional Array", one_d_array)

# 3. Two Dimensional Array
"""
Two Dimensional array are collection of 1-D array
It has both X-axis and y-axis.
It can move in 2 direction column and row
"""

two_d_array = np.array([[1, 2, 3], [10, 20, 30], [100, 200, 300]])
print("Two Dimensional Array \n", two_d_array)


# 3. Three Dimensional Array
"""
Three Dimensional array are collection of 3-d array
It has 3 axises, x-axis, y-axis and z-axis
"""

three_d_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("Three D array \n", three_d_array)

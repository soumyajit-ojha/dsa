"""
Array By Num py
    it take two parameter
    1. array object
    2. dtype: datatype of array(optional)
    - numpy array allow heterogenious element
"""

import numpy as np

my_arr = np.array([1, 2, 3, 4, 5, 6])
print("My array", my_arr)


# Create specific type array.
"""
To create such type array.
    - provide the second parameter dtype
    eg. my_arr = numpy.array([10, 20, 15], float)
        - this will convert all elements into float. if can't it retturn error
"""
my_float_arr = np.array(
    [
        1,
        2,
        3,
        4,
        5,
        6,
    ],
    float,
)
my_str_arr = np.array(
    [1, 2, 3, 4, "abcd", 5 + 60j],  # complex number
    str,
)

print("My float array", my_float_arr)
print("My string array", my_str_arr)


# Create a AP(arithmatic progressed array): nd-array (n-dimensional)
"""
To create such array numpy has a function "linspace".
This take three parameter
    1. starting point
    2. ending point (being included)
    3. partion size
"""

my_ap_array = np.linspace(10, 20, 5)
print(my_ap_array, type(my_ap_array))


# Create array by arange.
"""
To create an array with a arithmatic progress.
Thix takes 3 parameters.
    1. the start number
    2. the end number (not included)
    3. step size (different bw. two digits.)
"""

ranged_array = np.arange(10, 100, 10)  # here 100 not included
print("Ranged Array", ranged_array)

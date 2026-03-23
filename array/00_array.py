"""
Array:
    - contigious memory allocation
    - similar types of element

    Uses:
    - When we need to store multiple element having same datatype.
NOTE: In pyton we cann't use array directly.
    - we can use it by using by importing numpy or array module.

How to create an array.
    - import array or numpy
    import array

    - initalize an array
    arr = array.array(type_code, data_list)
    => type_code : this denote the datatype of array its going to hold
    => data_list : this is the actual data we are going to store.

"""

from array import array as arr

my_arr = arr("i", [10, 20, 30, 40, 50])
# print(my_arr)

# 0. Indexing
# print(my_arr[-1])

# 1. Reverse an array.
# my_arr.reverse()
# print(my_arr)


# 2. Insert an element to existing array/
my_arr.insert(0, 1000)
print(my_arr)

"""
NOTE: insert method's 1st parameter is index no and 2nd is value
        But we can't use -1 for last element. it will add to the second last.
        Use append method to add at the end of array.
"""
my_arr.append(999)
print(my_arr)


# 3. Copy an array.
type_code = my_arr.typecode
copied_array = arr(type_code, (i for i in my_arr))
print(copied_array)

# 4. delete an element POP.
# pop use index of element in array to remove an element.
# by default pop delete the last element and return it.
r = my_arr.pop(1)
print("Removed element", r)
print("after (pop) delete", my_arr)


# 5. Remove a element from array
# remove take an element from array to remove
my_arr.remove(1000)
print(my_arr)


# 6.Indexig in array
s1 = my_arr[2:5]
print("SLiced array -", s1)
s2 = my_arr[::-1]
print("Reversed array (by slicing) -", s2)

# 7. Index: get the index of element (if available)
ind = my_arr.index(999)
print("index of 999 is =", ind)

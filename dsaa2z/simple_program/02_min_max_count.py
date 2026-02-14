# Find the min count of a element in array also max count of an element in array


"""
Step 1. create a dictonary to track the each element repeatation {"element" : "repetation"}
Step 2. a) sort the dictionary in accending order and return the first element.
        b) compare all element frequency and return the min one and max one element.
"""


# get all element frequency
def get_frequency(arr: list) -> dict:
    frequency = {}
    for i in arr:
        frequency[i] = frequency.get(i, 0) + 1
    return frequency


def get_min_count(arr: list):
    freq_dict = get_frequency(arr)
    min_val = min(freq_dict.values())

    for k, v in freq_dict.items():
        if freq_dict[k] == min_val:
            return k
    return None


def get_max_count(arr: list):
    freq_dict = get_frequency(arr)
    max_val = max(freq_dict.values())

    for k, v in freq_dict.items():
        if freq_dict[k] == max_val:
            return k
    return None


arr = [10, 5, 5, 12, 6, 7, 7, 6, 12, 5]
min = get_min_count(arr=arr)
max = get_max_count(arr=arr)

print(min)
print(max)

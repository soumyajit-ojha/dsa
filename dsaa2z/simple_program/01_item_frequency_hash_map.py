# get item frequency by hash map.


def get_frequency(lst: list):
    dct = {}
    for item in lst:
        dct[item] = dct.get(item, 0) + 1
    return dct


num_list = [10, 14, 10, 15, 14, 15]
print(get_frequency(num_list))

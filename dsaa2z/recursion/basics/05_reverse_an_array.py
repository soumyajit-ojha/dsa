#  reverse an array


def reverse_array(arr: list) -> list:
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    if len(arr) <= 1:
        return arr

    return [arr[-1]] + reverse_array(arr[:-1])


l = [1, 2, 3]
print(reverse_array(arr=l))


def reverse_list(lst, index=0):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    if index >= len(lst) // 2:
        return lst

    lst[index], lst[-index - 1] = lst[-index - 1], lst[index]
    return reverse_list(lst, index + 1)


# Example
print(reverse_list([1, 2, 3, 4, 5]))

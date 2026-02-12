# sum of first n numbers


def sum_of_numbers(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must have to be a number.")
    if n == 1:
        return 1
    return n + sum_of_numbers(n - 1)


res = sum_of_numbers(3)
print(res)

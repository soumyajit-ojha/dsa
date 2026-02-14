# Print 1 to n with recursion


def print_num(
    n: int,
):
    if not isinstance(n, int):
        return TypeError("n must to be a integer.")
    if n == 1:
        return "1"
    return str(print_num(n - 1)) + "\n" + str(n)


res = print_num(5)
print(res)


# Print n to 1 with recursion


def print_num_invert(
    n: int,
):
    if not isinstance(n, int):
        return TypeError("n must to be a integer.")
    if n == 1:
        return "1"
    return str(n) + "\n" + str(print_num_invert(n - 1))


res = print_num_invert(5)
print(res)

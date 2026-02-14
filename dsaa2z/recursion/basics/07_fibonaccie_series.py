# fibonacci series


def fibonnacie_series(size):
    res = [0, 1]
    while size > 1:
        res += [res[-1] + res[-2]]
        size -= 1
    return res


print(fibonnacie_series(6))


def fib(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n < 0:
        raise ValueError("n must be >= 0")

    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)


print(fib(6))

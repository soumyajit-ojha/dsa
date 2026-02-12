# factorial of a number

def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must have to be a number.")

    # base condition
    if n == 1:
        return 1

    return n * factorial(n-1)


res = factorial(5)
print(res)

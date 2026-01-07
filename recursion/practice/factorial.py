def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return factorial(n-1) * n

res = factorial(5)
print(res)


def sum_numbers(n: int) -> int:
    # base condition
    if n <= 0:
        return 0
    return sum_numbers(n-1) + n

print(sum_numbers(5))

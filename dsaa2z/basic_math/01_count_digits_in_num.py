def count_digits(n: int) -> int:
    temp = n
    digits_counter = 0
    while temp > 0:
        temp = temp // 10
        digits_counter += 1
    return digits_counter

res = count_digits(n=5555)
print(res)

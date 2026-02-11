# length of a number
num = 1547


def count_len(n: int):
    len = 0
    while n > 0:
        res = n // 10
        len += 1
        n = res
    return len


print(count_len(1234))

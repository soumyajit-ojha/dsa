# Get all deviser of a number.
# to solve this we need to check from 1 to the current number with check if any number can devide the number return it.


def get_all_deviser(num: int) -> list[int]:
    res = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            if i == num // i:
                res.append(i)
            else:
                res.extend([i, num // i])
    return res


print(get_all_deviser(147))

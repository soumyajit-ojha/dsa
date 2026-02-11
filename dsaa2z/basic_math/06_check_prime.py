# check for a number either its a prime numbe or not.
# each prime nymbers are has only two deviser 1 and the number itself.


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(n=147))

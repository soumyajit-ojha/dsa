# Power of number
def power(base, exp) -> int:
    res = 1
    while exp > 0:
        if exp % 2 == 1:
            res = res * base
        
        base = base * base
        exp = exp // 2
    return res


p = power(base=2, exp=8)
print(p)

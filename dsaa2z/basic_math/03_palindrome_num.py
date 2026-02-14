def reverse_number(num: int):
    res = 0
    while num > 0:
        temp = num % 10
        num = num // 10
        res = (res*10) + temp
    return res        
n = 1234321
if n == reverse_number(num=n):
    print(True)
else:
    print(False)

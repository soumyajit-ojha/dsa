
# Reverse a number
# 1234 to 4321
# step1= reduce numbers from 1234 one after one from right side ( 4 -> 3 -> 2 -> 1)
#        we will use modulos operator to do this. (1234 % 10 = 4 and so on.)

# step2= after extracting numbers one after one we have to add them to result variable 0.
#        we will do this by multiplying 10 to that value then add that number.
#        res=0 => (res*10) + 4 = 4 
#        res=4 => (4*10) + 3 = 43 .... and so on.

def reverse_number(num: int):
    res = 0
    while num > 0:
        temp = num % 10
        num = num // 10
        res = (res*10) + temp
    return res        

print(reverse_number(556677))

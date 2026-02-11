# atmstrong number: the number is equal to sum of all its number's power to its lengths
# eg 153, len = 3
#   1**3 + 5**3 + 3**3 = 1 + 125 + 27 = 153

# 1. find the length of number. length = 3
# 2. extract each number from number by deviding 10, n = (153 % 10 = 3)
# 3. create a result variable with value 0. res = 0
# 4. add those number as per armstrong rules. res = res + (n**length)
# 5. repeat this process untill the main number becomes 0 with floor-division by 10
#           153 // 10
# 6. At last check for their value equality. number == res ?


def is_armstrong(num: int):
    length = len(str(num))
    res = 0
    n = num
    while num > 0:
        temp = num % 10
        res = res + (temp**length)
        num = num // 10
    return n == res


print(is_armstrong(153))

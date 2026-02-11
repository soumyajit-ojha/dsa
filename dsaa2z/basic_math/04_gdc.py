# to find the GCD of two numbers. we have to follow several steps
#   1. max number is dividend and min number is diviser.
#   2. divide max number with min number. if its reminder is zero then GCD is min number.
#   3. if it return a number then this reminder replaced to diviser and the older deviser (the min number) replaced to dividend.

# eg. 8 and 20
#   diviser = 8 (min num)
#   dividend = 20 (mix num)
#   20 % 8 = 4
#   => deviser = 4 (replace 8 to 4)
#   dividend = 8 (older deviser 8)
#   => 8 % 4 = 0
#   It return 0 so result will be "4"


def get_gcd(num1, num2):
    gcd = num1 if num1 < num2 else num2
    devidend = num1 if num1 > num2 else num2

    while devidend % gcd != 0:
        temp = gcd
        gcd = devidend % gcd
        devidend = temp
    return gcd

print(get_gcd(10,30))


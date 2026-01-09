# l, b = input().split()
def calculate_area(l, b):
    try:
        return int(l)*int(b)
    except:
        return "Error raised"
# print(calculate_area(l,b))

# The name of the person is Ali and the age is 30.
# name = input("Enter name: ")
# age = input("Enter age: ")

def print_details(name: str, age: str) -> str:
    if not name.isalpha():
        return "name must be string."
    if not age.isnumeric():
        return "age must be number."
    return "The name of the person is "+ str(name)+ " and the age is "+str(age)+"."
# print(print_details(name, age))

num1, num2 = input().strip().split()

def swap_vars(a,b):
    a = int(a)
    b = int(b)
    a,b = b,a
    return str(a)+" "+str(b)

print(swap_vars(num1, num2))

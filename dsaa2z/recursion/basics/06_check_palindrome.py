# Check if either the string is palindrome or not.

# Iterative way
st = "applelppa"

# def is_palindrome(st):
#     s,l = 0, -1
#     while abs(l) > s:
#         if st[s] != st[l]:
#             return False
#         s += 1
#         l -= 1
#         return True

# print(is_palindrome(st))


# Recursive way
def is_palindrome(s, e, st):
    if e < s:
        return True
    if st[s] != st[e]:
        return False
    return is_palindrome(s=s + 1, e=e - 1, st=st)

print(
    is_palindrome(s=0, e=-1, st=st)
)

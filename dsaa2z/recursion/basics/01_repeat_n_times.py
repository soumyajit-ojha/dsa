# Repeat a statement n times.

def repeat(n: int, text: str) -> str:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n < 0:
        raise ValueError("n must be > 0")

    if n == 0:
        return ""

    return text + "\n" + repeat(n - 1, text)


res = repeat(5, "Hello")
print(res)
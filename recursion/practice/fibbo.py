def fibbonacci(n: int):
    # base condition
    if n <= 1:
        return 1
    
    return fibbonacci(n-1) + fibbonacci(n-2)


def fibbo(n: int):
    ser = [0, 1]
    for i in range(n - 2):
        ser.append(ser[-1] + ser[-2])

    return ser


print(fibbonacci(5))

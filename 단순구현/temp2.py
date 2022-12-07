L = [0] * (100)
def fibo(i):
    global L
    if i == 1 or i == 2:
        return 1
    if L[i] != 0:
        return L[i]
    else:
        L[i] = fibo(i-1) + fibo(i-2)
        return L[i]
for i in range(1, 11):
    result = fibo(i)
    print(f"fibo({i}) = {result}")
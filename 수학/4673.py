import sys
input = sys.stdin.readline
L = [False] * 10001
def func(N):
    return N + sum(map(int, list(str(N))))
for i in range(1, 10001):
    M = func(i)
    if M < len(L):
        L[M] = True
for i in range(1, 10001):
    if L[i] is False:
        print(i)
import sys
input = sys.stdin.readline
T = int(input())
def factorial(n):
    S = 1
    for i in range(2, n+1):
        S = S * i
    return S
def C(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))
for _ in range(T):
    N, M = map(int, input().split())
    print(C(M, N))

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    L = [0] * (N+1)
    L[1] = 1
    L[2] = 1
    for i in range(3, N+1):
        L[i] = L[i-2]+L[i-3]
    print(L[N])


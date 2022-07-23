import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
L = [0] * N 
L[0] = A[0]
for i in range(1, N):
    L[i] = A[i] + max(0, L[i-1])
print(max(L))


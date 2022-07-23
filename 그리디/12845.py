import sys
input = sys.stdin.readline
N = int(input())
L = list(map(int, input().split()))
M = max(L)
print(M * (N-1) + sum(L) - M)

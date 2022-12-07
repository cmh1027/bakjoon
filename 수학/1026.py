import sys
input = sys.stdin.readline
N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
S = 0
for a, b in zip(A, reversed(B)):
    S += a * b
print(S)
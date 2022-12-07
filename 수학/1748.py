import sys
input = sys.stdin.readline
N = int(input())
length = len(str(N))
i = 1
S = 0
m = 9
while i < length:
    S += i * m
    i = i + 1
    m = m * 10
S += (N - pow(10, i-1) + 1) * i
print(S)
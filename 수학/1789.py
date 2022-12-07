import sys
input = sys.stdin.readline
N = int(input())
i = 1
while i * (i+1) // 2 <= N:
    i = i + 1
print(i-1)
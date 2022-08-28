import sys
input = sys.stdin.readline
A = int(input())
B = list(map(int, list(input().strip())))
print(B[2] * A)
print(B[1] * A)
print(B[0] * A)
print(B[2] * A + B[1] * A * 10 + B[0] * A * 100)
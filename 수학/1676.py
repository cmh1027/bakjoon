import sys
input = sys.stdin.readline
N = int(input())
D = 5
five = 0
while D <= N:
    five += N // D
    D *= 5
print(five)
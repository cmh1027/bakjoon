import sys
input = sys.stdin.readline
E, S, M = map(int, input().split())
b = 0
while not ((28 * b + S - E) % 15 == 0 and (28 * b + S - M) % 19 == 0):
    b = b + 1
print(28 * b + S)
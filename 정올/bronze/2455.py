import sys
input = sys.stdin.readline
current = 0
M = -1
for _ in range(4):
    A, B = map(int, input().split())
    current = current + (B-A)
    if M < current:
        M = current
print(M)
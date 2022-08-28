import sys
input = sys.stdin.readline
N = int(input())
belts = []
for _ in range(N):
    belts.append(list(map(int, input().split())))
direction = 1
value = 1
for a, b, D in belts:
    if D == 1:
        direction *= -1
    value = value * b // a
if direction == -1:
    direction = 1
else:
    direction = 0
print(direction, value)

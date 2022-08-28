import sys
from collections import Counter
input = sys.stdin.readline
def rotate(direction, length, front):
    while direction[0] != front:
        direction.append(direction[0])
        del direction[0]
        length.append(length[0])
        del length[0]
A = Counter([3,1,3,1,4,2]) # ┐
B = Counter([3,1,4,1,4,2]) # ┌
C = Counter([3,2,3,1,4,2]) # ┘
D = Counter([3,1,4,2,4,2]) # └
direction = []
length = []
K = int(input())
for _ in range(6):
    x, y = map(int, input().split())
    direction.append(x)
    length.append(y)
directionCounter = Counter(direction)
if directionCounter == A:
    rotate(direction, length, 2)
    print(K * (length[0] * length[5] - length[2] * length[3]))
elif directionCounter == B:
    rotate(direction, length, 3)
    print(K * (length[0] * length[5] - length[2] * length[3]))
elif directionCounter == C:
    rotate(direction, length, 1)
    print(K * (length[0] * length[1] - length[3] * length[4]))
else:
    rotate(direction, length, 3)
    print(K * (length[0] * length[1] - length[3] * length[4]))
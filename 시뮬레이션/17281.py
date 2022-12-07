# pypy말고 python으로 제출하면 시간초과
import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
L = []
for _ in range(N):
    L.append(list(map(int, input().split())))
C = permutations([1,2,3,4,5,6,7,8], 8)
maximum = 0
for order in C:
    order = list(order)
    order.insert(3, 0)
    inning = 0
    score = 0
    i = 0
    while inning < N:
        ### inning Start ###
        out = 0
        b1, b2, b3 = 0, 0, 0 # 리스트로 두면 시간초과남
        while True:
            num = L[inning][order[i]]
            i = (i + 1) % 9
            if num == 0:
                out += 1
                if out == 3:
                    break
            elif num == 1:
                b1, b2, b3, score = 1, b1, b2, score + b3
            elif num == 2:
                b1, b2, b3, score = 0, 1, b1, score + b2 + b3
            elif num == 3:
                b1, b2, b3, score = 0, 0, 1, score + b1 + b2 + b3
            else:
                b1, b2, b3, score = 0, 0, 0, score + b1 + b2 + b3 + 1
        inning += 1
    if maximum < score:
        maximum = score
print(maximum)
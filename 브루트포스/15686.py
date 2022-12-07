import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())
L = []
for _ in range(N):
    L.append(list(map(int, input().split())))
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if L[i][j] == 1:
            house.append((i, j))
        elif L[i][j] == 2:
            chicken.append((i, j))
minVal = float('inf')
for chickens in combinations(chicken, M):
    distance = 0
    for hx, hy in house:
        minDistance = float('inf')
        for cx, cy in chickens:
            minDistance = min(minDistance, abs(hx-cx) + abs(hy-cy))
        distance += minDistance
    minVal = min(minVal, distance)
print(minVal)
# pypy말고 python으로 제출하면 시간초과
import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())
graph = []
nonsafe = 3 # always added 3 walls
virus = []
candidates = set([(i, j) for i in range(N) for j in range(M)]) # coordinates in which a wall can be
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = set()
maximum = 0
def isValidCoord(i, j):
    global N, M
    return 0 <= i < N and 0 <= j < M
for _ in range(N):
    graph.append(list(map(int, input().split())))
for i in range(N):
    for j in range(M):
        if graph[i][j] > 0: # wall, virus
            nonsafe += 1
            candidates.remove((i, j))
            visited.add((i, j))
        if graph[i][j] == 2: # virus
            virus.append((i, j))
def dfs(i, j, visited):
    add = 1
    for di, dj in d:
        if (i+di, j+dj) not in visited and isValidCoord(i+di, j+dj) is True:
            visited.add((i+di, j+dj))   
            add += dfs(i+di, j+dj, visited)
    return add
for walls in combinations(candidates, 3):
    for i, j in walls:
        visited.add((i, j))
    S = 0
    V = visited.copy()
    for vi, vj in virus:
        S += dfs(vi, vj, V) - 1 # exclude virus itself
    maximum = max(maximum, N*M - (nonsafe+S))
    for i, j in walls:
        visited.remove((i, j))
print(maximum)
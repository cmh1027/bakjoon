import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
maximum = -1
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d_comb = list(combinations(d, 3))
def isValidCoord(i, j):
    global N, M
    return 0 <= i < N and 0 <= j < M
def dfs(i, j, depth, S, visited):
    global maximum, graph, d, d_comb
    if depth == 4:
        maximum = max(maximum, S)
        return
    elif depth == 1: # 凸 shape
        for comb in d_comb:
            for di, dj in comb:
                if isValidCoord(i+di, j+dj) is False:
                    break
            else:
                maximum = max(maximum, S+sum([graph[i+di][j+dj] for di, dj in comb]))
    for di, dj in d:
        if isValidCoord(i+di, j+dj) is False or (i+di, j+dj) in visited:
            continue
        visited.add((i+di, j+dj))
        dfs(i+di, j+dj, depth+1, S+graph[i+di][j+dj], visited)
        visited.remove((i+di, j+dj))
for i in range(N):
    for j in range(M):
        dfs(i, j, 1, graph[i][j], {(i, j)})
print(maximum)
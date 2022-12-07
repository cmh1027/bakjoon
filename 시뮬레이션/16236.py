# pypy말고 python으로 제출하면 시간초과
import sys
input = sys.stdin.readline
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
fish = []
sharkLv = 2
hunger = 0
minute = 0
INF = float('inf')
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(N):
    for j in range(N):
        if 0 < graph[i][j] < 9:
            fish.append((i, j))
        if graph[i][j] == 9:
            si, sj = i, j
def isValidCoord(i, j):
    global N
    return 0 <= i < N and 0 <= j < N
def getDistance(si, sj, fi, fj):
    global graph, d, sharkLv
    distance = [[INF] * N for _ in range(N)]
    distance[si][sj] = 0
    visited = [[False] * N for _ in range(N)]
    visited[si][sj] = True
    queue = [(si, sj)]
    while len(queue) > 0:
        i, j = queue.pop(0)
        if i == fi and j == fj:
            return distance[i][j]
        for di, dj in d:
            if isValidCoord(i+di, j+dj) is False or visited[i+di][j+dj] is True or graph[i+di][j+dj] > sharkLv:
                continue
            visited[i+di][j+dj] = True
            distance[i+di][j+dj] = distance[i][j] + 1
            queue.append((i+di, j+dj))
    return INF
def update(fi, fj, ci, cj, minD):
    global si, sj
    newD = getDistance(si, sj, fi, fj)
    if newD < minD:
        return fi, fj, newD
    elif newD == minD:
        if fi < ci:
            return fi, fj, newD
        elif fi == ci:
            if fj < cj:
                return fi, fj, newD
    return ci, cj, minD
def moveTo(ci, cj):
    global si, sj, fish
    graph[si][sj] = 0 # set zero the place where the shark was
    graph[ci][cj] = 9 # set nine the place where the shark is
    si, sj = ci, cj # update shark coordinates
    fish.remove((ci, cj))

while True:
    ci, cj = INF, INF
    minD = INF
    for fi, fj in fish:
        if graph[fi][fj] >= sharkLv:
            continue
        ci, cj, minD = update(fi, fj, ci, cj, minD)
    if minD == INF:
        break
    moveTo(ci, cj)
    minute += minD
    hunger, sharkLv = (hunger+1) % sharkLv, sharkLv + (hunger+1) // sharkLv
print(minute)
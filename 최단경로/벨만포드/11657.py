import sys

inf = float('inf')
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))
S = 1
distance = [inf] * (N+1)
distance[S] = 0
for _ in range(N):
    for start in range(1, N+1):
        for end, weight in graph[start]:
            if distance[start] + weight < distance[end]:
                distance[end] = distance[start] + weight
for _ in range(N):
    for start in range(1, N+1):
        for end, weight in graph[start]:
            if distance[start] + weight < distance[end]:
                print(-1)
                exit(0)
for i in range(2, N+1):
    if distance[i] == inf:
        print(-1)
    else:
        print(distance[i])
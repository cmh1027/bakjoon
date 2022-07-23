import sys

inf = float('inf')
input = sys.stdin.readline
TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M): # load 
        start, end, weight = map(int, input().split())
        graph[start].append((end, weight))
        graph[end].append((start, weight))
    for _ in range(W): # wormhole
        start, end, weight = map(int, input().split())
        graph[start].append((end, -weight))
    S = 1
    distance = [2200000000] * (N+1)
    distance[S] = 0
    cycle = False
    for _ in range(N):
        for start in range(1, N+1):
            for end, weight in graph[start]:
                if distance[start] + weight < distance[end]:
                    distance[end] = distance[start] + weight

    for _ in range(N):
        for start in range(1, N+1):
            for end, weight in graph[start]:
                if distance[start] + weight < distance[end]:
                    cycle = True
    if cycle is True:
        print("YES")
    else:
        print("NO")
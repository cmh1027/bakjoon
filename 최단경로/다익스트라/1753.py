import sys
import heapq
inf = float('inf')
input = sys.stdin.readline
V, E = map(int, input().split()) # node, edge
S = int(input()) # start point
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split()) # u : start point, v : end point, w : weight
    graph[u].append((v, w))
distance = [inf] * (V+1)
distance[S] = 0
heap = []
heapq.heappush(heap,(0, S))
while len(heap) > 0:
    weight, node = heapq.heappop(heap)
    if distance[node] >= weight:
        for v, w in graph[node]:
            if weight + w < distance[v]: # weight : A => D, w : D -> B, distance[v] : A => B
                distance[v] = weight + w
                heapq.heappush(heap, (weight+w, v))
for i in range(1,V+1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])
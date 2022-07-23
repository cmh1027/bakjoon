import sys
import heapq
inf = float('inf')
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w)) # u->v
    graph[v].append((u, w)) # v->u
v1, v2 = map(int, input().split())
distance = [[inf] * (V+1) for _ in range(3)] # 1, v1, v2
distance[0][1] = 0 # distance[0] : 1을 시작점으로 하는 최소거리
distance[1][v1] = 0 # distance[1] : v1을 시작점으로 하는 최소거리
distance[2][v2] = 0 # distance[2] : v2를 시작점으로 하는 최소거리

for i, S in enumerate([1, v1, v2]): # [(0,1), (1,v1), (2,v2)]
    heap = []
    heapq.heappush(heap,(0, S))
    while len(heap) > 0:
        weight, node = heapq.heappop(heap)
        if distance[i][node] >= weight:
            for v, w in graph[node]:
                if weight + w < distance[i][v]:
                    distance[i][v] = weight + w
                    heapq.heappush(heap, (weight+w, v))

minimum = min(distance[0][v1] + distance[1][v2] + distance[2][V], distance[0][v2] + distance[2][v1] + distance[1][V])
# distance[0][v1] 1->v1
# distance[1][v2] v1->v2
# distance[2][V] v2->V
# distance[0][v2] 1->v2
# distance[2][v1] v2->v1
# distance[1][V] v1->V
if minimum == inf:
    print(-1)
else:
    print(minimum)
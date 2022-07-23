import sys
import heapq
def update(graph, u, v, w):
    if u not in graph:
        graph[u] = {}
    if v in graph[u]:
        if w < graph[u][v]:
            graph[u][v] = w
    else:
        graph[u][v] = w

inf = float('inf')
input = sys.stdin.readline
N, D = map(int, input().split()) # edge count, end point
S = 0
graph = {} # dictionary
points = {0, D} # set

for _ in range(N):
    u, v, w = map(int, input().split())
    points.add(u)
    points.add(v)
    update(graph, u, v, w)

points = sorted(list(points))
for i in points:
    if i not in graph:
        graph[i] = {}
# graph[max(points)] = {}
        
for i in range(len(points)-1):
    u, v, w = points[i], points[i+1], points[i+1]-points[i]
    update(graph, u, v, w)

distance = {}
for i in points:
    if i == 0:
        distance[i] = 0
    else:
        distance[i] = inf
heap = []
heapq.heappush(heap,(0, S))
while len(heap) > 0:
    weight, node = heapq.heappop(heap)
    if distance[node] >= weight:
        for v, w in graph[node].items(): # items() 주의! why? graph[node]가 dictionary
            if weight + w < distance[v]:
                distance[v] = weight + w
                heapq.heappush(heap, (weight+w, v))
print(distance[D])
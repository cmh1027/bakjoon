import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
queue = [1]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
while len(queue) > 0:
    front, queue = queue[0], queue[1:]
    if visited[front] is False:
        visited[front] = True
        queue.extend(graph[front])
print(sum(visited) - 1)
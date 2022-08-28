x = int(input())
y = int(input())
graph = [[] for _ in range(x+1)]
for _ in range(y):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = [1]
visited = [False] * 6
while len(queue) > 0:
    front, queue = queue[0], queue[1:]
    if visited[front] is False:
        visited[front] = True
        queue.extend(graph[front])
        print(front, end=" ")
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = []
xrow = set()
xcol = set()
for row in range(N):
    graph.append(list(input().strip()))
for row in range(N):
    for col in range(M):
        if graph[row][col] == 'X':
            xrow.add(row)
            xcol.add(col)
print(max(N-len(xrow), M-len(xcol)))
    
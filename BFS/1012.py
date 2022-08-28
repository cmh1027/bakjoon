import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    visited = [[False] * N for _ in range(M)]
    graph = [[0] * N for _ in range(M)]
    for _ in range(K):
        m, n = map(int, input().split())
        graph[m][n] = 1
    queue = []
    connected = 0
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i in range(M):
        for j in range(N):
            if visited[i][j] is False and graph[i][j] == 1:
                connected += 1
                queue = [(i, j)]
                while len(queue) > 0:
                    f_i, f_j = queue.pop(0)
                    if visited[f_i][f_j] is False:
                        visited[f_i][f_j] = True
                        for d_i, d_j in d:
                            if 0 <= f_i+d_i < M and 0 <= f_j+d_j < N and visited[f_i+d_i][f_j+d_j] is False and graph[f_i+d_i][f_j+d_j] == 1:
                                queue.append((f_i+d_i, f_j+d_j))
    print(connected)

            
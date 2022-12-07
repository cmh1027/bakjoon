import sys
input = sys.stdin.readline
N, M, R = map(int, input().split())
X = []
for _ in range(N):
    X.append(list(map(int, input().split())))
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def isValid(r, c):
    global N, M, newX
    return 0 <= r < N and 0 <= c < M and newX[r][c] == 0
for _ in range(R):
    newX = [[0] * M for _ in range(N)]
    for s in range(min(N, M)):
        if newX[s][s] != 0:
            break
        r, c = s, s
        for dr, dc in d:
            while True:
                if not isValid(r + dr, c + dc):
                    break
                newX[r+dr][c+dc] = X[r][c]
                r, c = r + dr, c + dc
    for i in range(N):
        for j in range(M):
            X[i][j] = newX[i][j]
for row in X:
    print(*row)
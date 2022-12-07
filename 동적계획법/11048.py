import sys
input = sys.stdin.readline
N, M = map(int, input().split())
L = []
dp = [[0] * M for _ in range(N)]
for _ in range(N):
    L.append(list(map(int, input().split())))
dp[0][0] = L[0][0]
for i in range(N):
    for j in range(M):
        if j-1 >= 0:
            dp[i][j] = dp[i][j-1] + L[i][j]
        if i-1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + L[i][j])
        if i-1 >= 0 and j-1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + L[i][j])
print(dp[N-1][M-1])
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
dp = [[0] * 201 for _ in range(201)]
mod = 1000000000
# dp[i][j] : i개의 수로 j를 만드는 경우의 수
# DP[K][N] = DP[K-1][0] + DP[K-1][1] + .... + DP[K-1][N]
for i in range(N+1):
    dp[1][i] = 1
for k in range(2, K+1):
    for n in range(N+1):
        for j in range(n+1):
            dp[k][n] = (dp[k][n] + dp[k-1][j]) % mod
print(dp[K][N])
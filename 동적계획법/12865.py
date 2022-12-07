import sys
input = sys.stdin.readline
N, K = map(int, input().split())
W, V = [0], [0]
dp = [[0] * 100001 for _ in range(101)] # 101 * 100001
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

# dp[i][j] : i번째 item을 보고 있는 상황에서 knapsack의 무게가 K일때의 최댓값
for i in range(1, N+1):
    for j in range(1, K+1):
        if j - W[i] >= 0: # enough space
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W[i]] + V[i])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][K])

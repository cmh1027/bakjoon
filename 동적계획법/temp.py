import sys
input = sys.stdin.readline
N = int(input())
X = []
for _ in range(N):
    X.append(int(input()))
dp = [0] * N
dp[0] = X[0]
if N >= 2:
    dp[1] = X[0] + X[1]
if N >= 3:
    dp[2] = max(dp[1], dp[0]+X[2])
for i in range(3, N):
    dp[i] = max(max(dp[i-1], dp[i-2]+X[i]), dp[i-3]+X[i-1]+X[i])
print(dp[N-1])

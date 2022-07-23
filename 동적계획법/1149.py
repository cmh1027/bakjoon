import sys
input = sys.stdin.readline
N = int(input())
L = []
for _ in range(N):
    L.append(list(map(int, input().split())))
dp = [[0] * 3 for _ in range(N)]
dp[0] = L[0]
for i in range(1, N):
    dp[i][0] = L[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = L[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = L[i][2] + min(dp[i-1][0], dp[i-1][1])
print(min(dp[N-1]))
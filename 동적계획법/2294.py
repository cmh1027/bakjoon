import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = [0]
for _ in range(n):
    coins.append(int(input()))
dp = [10001] * (k+1)
dp[0] = 0
for i in range(1, n+1):
    for j in range(1, k+1):
        if j - coins[i] >= 0:
            dp[j] = min(dp[j], dp[j-coins[i]]+1)
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
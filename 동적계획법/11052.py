import sys
input = sys.stdin.readline
N = int(input())
L = [0] + list(map(int, input().split()))
dp = [0] * (N+1)
dp[1] = L[1]
for i in range(2, N+1):
    dp[i] = L[i]
    for j in range(1, i):
        dp[i] = max(dp[i], dp[j] + dp[i-j])
print(dp[N]) 
import sys
input = sys.stdin.readline
N = int(input())
dp = [1, 1, 1]
# O X / X O / X X
for i in range(1, N):
    dp[0], dp[1], dp[2] = dp[1] + dp[2], dp[0] + dp[2], dp[0] + dp[1] + dp[2]
print(sum(dp) % 9901)
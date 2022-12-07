# pypy로 제출해야함
import sys
input = sys.stdin.readline
N = int(input())
dp = list(range(0, N+1))
for i in range(1, N+1):
    num = 1
    minimum = dp[i]
    while num * num <= i:
        minimum = min(minimum, dp[i - num * num] + 1)
        num = num + 1
    dp[i] = minimum
print(dp[N])
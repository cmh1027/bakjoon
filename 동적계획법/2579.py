import sys
input = sys.stdin.readline
N = int(input())
stairs = [0] * (N+1)
dp = [0] * (N+1)
for i in range(1, N+1):
    stairs[i] = int(input())
dp[1] = stairs[1]
if N>=2:
    dp[2] = stairs[1] + stairs[2]
for n in range(3, N+1):
    dp[n] = max(dp[n-3] + stairs[n-1] + stairs[n], dp[n-2] + stairs[n])
print(dp[N])

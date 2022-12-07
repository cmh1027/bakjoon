import sys
input = sys.stdin.readline
N = int(input())
wine = [0] * (N+1)
dp = [0] * (N+1)
for i in range(1, N+1):
    wine[i] = int(input())
dp[1] = wine[1]
if N>=2:
    dp[2] = wine[1] + wine[2]
if N>=3:
    dp[3] = max(dp[1] + wine[3], dp[2])
for n in range(4, N+1):
    if n < N:
        dp[n] = max(max(dp[n-3] + wine[n-1] + wine[n], dp[n-2] + wine[n]), dp[n-1])
    else:
        dp[n] = max(dp[n-3] + wine[n-1] + wine[n], dp[n-2] + wine[n])
print(dp[N])

import sys
input=sys.stdin.readline
n=int(input())
wine,dp=[0]*10001,[0]*10001
for i in range(1,n+1):
    wine[i]=int(input())
dp[1],dp[2]=wine[1],wine[1]+wine[2]
dp[3]=max(dp[2],wine[1]+wine[3],wine[2]+wine[3])
for i in range(4,n+1):
    dp[i]=max(dp[i-1],dp[i-2]+wine[i],dp[i-3]+wine[i]+wine[i-1])
print(dp[n]) 
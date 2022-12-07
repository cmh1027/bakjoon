import sys
input = sys.stdin.readline
N = int(input())
T, P = [0], [0]
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
dp = [0] * (N+2)
for i in reversed(range(1, N+1)):
    if i + T[i] - 1 > N:
        if i + 1 <= N:
            dp[i] = dp[i+1]
        else:
            dp[i] = 0
    else:
        dp[i] = max(dp[i+1], P[i] + dp[i+T[i]])
print(dp[1])
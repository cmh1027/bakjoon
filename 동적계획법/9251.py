import sys
input = sys.stdin.readline
S1 = input().strip()
S2 = input().strip()
L1 = len(S1)
L2 = len(S2)
dp = [[0] * (L2+1) for _ in range(L1+1)]
for i in range(1, L1+1) :
    for j in range(1, L2+1):
        if S1[i-1] == S2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp[L1][L2])
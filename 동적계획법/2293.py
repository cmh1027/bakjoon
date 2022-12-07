import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = [0]
for _ in range(n):
    coins.append(int(input()))
dp = [0] * 10001
dp[0] = 1

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= coins[i]:
            dp[j] = dp[j] + dp[j - coins[i]]
print(dp[k])

# D(i, k) =
#         k   0   1   2   3   4   5   6   7   8   9   10
# c(0)    [0] 1   0   0   0   0   0   0   0   0   0   0
# c(1)    [1] 1   1   1   1   1   1   1   1   1   1   1
# c(2)    [2] 1   1   2   2   3   3   4   4   5   5   6
# c(3)    [5] 1   1   2   2   3   4   5   6   7   8   10

# dp = [[0] * 10001 for _ in range(101)]
# for i in range(1, n+1):
#     dp[i][0] = 1

# for i in range(1, n+1):
#     for j in range(1, k+1):
#         if j >= coins[i]:
#             dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
#         else:
#             dp[i][j] = dp[i-1][j]
# print(dp[n][k])
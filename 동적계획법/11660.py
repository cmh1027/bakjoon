import sys
input = sys.stdin.readline
N, M = map(int, input().split())
mat, dp = [], []
for _ in range(N):
    mat.append(list(map(int, input().split())))
    dp.append([0] * N)
dp[0][0] = mat[0][0]
for row in range(1, N):
    dp[row][0] = dp[row-1][0] + mat[row][0]
for col in range(1, N):
    dp[0][col] = dp[0][col-1] + mat[0][col]
for row in range(1, N):
    for col in range(1, N):
        dp[row][col] = dp[row][col-1] + dp[row-1][col] - dp[row-1][col-1] + mat[row][col]
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    answer = dp[x2][y2]
    if x1 >= 1:
        answer -= dp[x1-1][y2]
    if y1 >= 1:
        answer -= dp[x2][y1-1]
    if x1 >= 1 and y1 >= 1:
        answer += dp[x1-1][y1-1]
    print(answer)
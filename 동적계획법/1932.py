import sys
input = sys.stdin.readline
N = int(input())
triangle = []
for _ in range(N):
    triangle.append(list(map(int, input().split())))
dp = []
for i in range(1, N+1):
    dp.append([0] * i)
dp[0][0] = triangle[0][0]
for i in range(1, N):
    for j in range(i+1):
        if j == 0: # 왼쪽
            dp[i][j] = triangle[i][j] + dp[i-1][j]
        elif j == i: # 오른쪽
            dp[i][j] = triangle[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[N-1]))

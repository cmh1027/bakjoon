T = int(input())
inputs = []
for _ in range(T):
    inputs.append(int(input()))
N = max(inputs)
dp = [0] * (N+1)
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, N+1):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009
for num in inputs:
    print(dp[num])
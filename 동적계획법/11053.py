import sys

input = sys.stdin.readline
N = int(input())
L = list(map(int, input().split()))
dp = [0 for _ in range(N)]
for i in range(N):
    dp[i] = 1 # Initialization
    for j in range(i):
        if L[j] < L[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

# def binarySearch(L, left, right, value):
#     while left < right:
#         mid = (left + right) // 2
#         if L[mid] < value:
#             left = mid + 1
#         else:
#             right = mid
#     return right

# LIS = [L[0]]
# for i in range(1, N):
#     if LIS[-1] < L[i]:
#         LIS.append(L[i])
#     else:
#         index = binarySearch(LIS, 0, len(LIS)-1, L[i])
#         LIS[index] = L[i]
# print(len(LIS))
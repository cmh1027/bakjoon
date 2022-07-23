import sys
input = sys.stdin.readline
N = int(input())
# 반복
# a, b = 1, 1
# for _ in range(1, N):
#     a, b = b, (a + b) % 15746
L = [0] * (N+1)
L[1] = 1
L[2] = 2
for i in range(3, N+1):
    L[i] = (L[i-1]+L[i-2]) % 15746
print(L[i])
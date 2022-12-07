import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
X = [[0] * N for _ in range(N)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
r, c = N//2, N//2
num = 1
X[r][c] = num
num = num + 1
if K == 1:
    ans_r, ans_c = r, c
for i in range(1, N//2+1):
    r, c = r - 1, c - 1
    for direction in d:
        dr, dc = direction
        for _ in range(2*i):
            r, c = r + dr, c + dc
            X[r][c] = num
            if K == num:
                ans_r, ans_c = r, c
            num = num + 1
for row in X:
    print(*row)
print(ans_r+1, ans_c+1)
import sys

input = sys.stdin.readline
R, C = map(int, input().split())
W = int(input())
L = [[-1] * C for _ in range(R)]
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
m = 0
count = 1
r, c = 0, 0
def isValid(r, c, R, C):
    return 0 <= r < R and 0 <= c < C
while count <= R * C:
    L[r][c] = count
    if count == W:
        print(r+1, c+1)
        exit(0)
    count = count + 1
    dr, dc = move[m]
    if not isValid(r+dr, c+dc, R, C) or L[r+dr][c+dc] != -1:
        m = (m+1) % 4
        dr, dc = move[m]
    r, c = r+dr, c+dc
print(0)
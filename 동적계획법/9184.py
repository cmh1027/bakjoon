import sys

W = [[[0]*21 for _ in range(21)] for _ in range(21)]
def f(a, b, c):
    global W
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if W[a][b][c]:
        return W[a][b][c]
    else:
        if a < b < c:
            W[a][b][c] = f(a, b, c-1) + f(a, b-1, c-1) - f(a, b-1, c)
            return W[a][b][c]
        else:
            W[a][b][c] = f(a-1, b, c) + f(a-1, b-1, c) + f(a-1, b, c-1) - f(a-1, b-1, c-1)
            return W[a][b][c]

input = sys.stdin.readline
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        if a <= 0 or b <= 0 or c <= 0:
            Z = 1
        elif a > 20 or b > 20 or c > 20:
            Z = f(20, 20, 20)
        else:
            Z = f(a, b, c)
        print("w(%d, %d, %d) = %d"%(a, b, c, Z))
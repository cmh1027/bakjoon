import sys
input = sys.stdin.readline
N = int(input())
M = [[' '] * N for _ in range(N)]
def func(row, col, N):
    global M
    if N == 1:
        M[row][col] = '*'
    else:
        func(row, col, N//3)
        func(row, col+N//3, N//3)
        func(row, col+2*N//3, N//3)
        func(row+N//3, col, N//3)
        func(row+N//3, col+2*N//3, N//3)
        func(row+2*N//3, col, N//3)
        func(row+2*N//3, col+N//3, N//3)
        func(row+2*N//3, col+2*N//3, N//3)
func(0, 0, N)
for R in M:
    print(''.join(R))
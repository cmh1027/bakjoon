import sys
import math
input = sys.stdin.readline
N = int(input())
n = int(math.log2(N // 3))
R = 5 + 6 * (2**n - 1)
M = [[' '] * R for _ in range(N)]
def func(row, col, N):
    global M
    if N == 0:
        M[row][col] = '*'
        for c in range(-1, 2, 2):
            M[row+1][col+c] = '*'
        for c in range(-2, 3):
            M[row+2][col+c] = '*'
    else:
        func(row, col, N-1)
        func(row+3*(2**(N-1)), col-3*(2**(N-1)), N-1)
        func(row+3*(2**(N-1)), col+3*(2**(N-1)), N-1)
func(0, R//2, n)
for R in M:
    print(''.join(R))
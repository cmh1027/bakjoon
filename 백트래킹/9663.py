# pypy말고 python으로 제출하면 시간초과
import sys
input = sys.stdin.readline
N = int(input())
count = 0
def recursion(row, cols):
    global N, count
    if row == N:
        count += 1
        return
    for col in range(N):
        for r in range(row):
            if col == cols[r] or row - col == r - cols[r] or row + col == r + cols[r]:
                break
        else:
            cols[row] = col
            recursion(row+1, cols)

recursion(0, [0] * N)
print(count)
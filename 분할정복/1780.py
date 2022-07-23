import sys

input = sys.stdin.readline
N = int(input())
mat = [[] for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    mat[i] = row
minus, zero, plus = 0, 0, 0

def allSameNumber(mat, startRow, startCol, N):
    number = mat[startRow][startCol]
    for i in range(startRow, startRow+N):
        for j in range(startCol, startCol+N):
            if mat[i][j] != number:
                return False
    return True

def divide(mat, startRow, startCol, N):
    global minus, zero, plus
    if allSameNumber(mat, startRow, startCol, N) is True:
        num = mat[startRow][startCol]
        if num == -1:
            minus += 1
        elif num == 0:
            zero += 1
        else:
            plus += 1
        return
    d = N // 3
    for i in range(3):
        for j in range(3):
            divide(mat, startRow+i*d, startCol+j*d, N//3)

divide(mat, 0, 0, N)
print(minus)
print(zero)
print(plus)
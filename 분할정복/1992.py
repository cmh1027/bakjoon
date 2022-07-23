import sys
def encode(mat, startRow, startCol, endRow, endCol):
    if startRow == endRow and startCol == endCol:
        return mat[startRow][startCol]
    midRow = (startRow + endRow) // 2
    midCol = (startCol + endCol) // 2
    a = encode(mat, startRow, startCol, midRow, midCol) # 좌상단
    b = encode(mat, startRow, midCol+1, midRow, endCol) # 우상단
    c = encode(mat, midRow+1, startCol, endRow, midCol) # 좌하단
    d = encode(mat, midRow+1, midCol+1, endRow, endCol) # 우하단
    if a == b == c == d and a.isdigit():
        return a
    else:
        return '(' + a + b + c + d + ')'


input = sys.stdin.readline
N = int(input())
mat = [[] for _ in range(N)]
for i in range(N):
    row = list(input().strip())
    mat[i] = row
print(encode(mat, 0, 0, N-1, N-1))

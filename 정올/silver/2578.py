import sys
input = sys.stdin.readline
def garo(check, r):
    for c in range(5):
        if check[r][c] is False:
            return False
    return True

def sero(check, c):
    for r in range(5):
        if check[r][c] is False:
            return False
    return True

def leftDiagonal(check):
    for r in range(5):
        if check[r][r] is False:
            return False
    return True

def rightDiagonal(check):
    for r in range(5):
        if check[r][4-r] is False:
            return False
    return True

coord = {}
check = [[False] * 5 for _ in range(5)]
count = 0
for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        coord[row[j]] = (i,j)
for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        pick = row[j]
        r, c = coord[pick]
        check[r][c] = True
        if garo(check, r):
            count = count + 1
        if sero(check, c):
            count = count + 1
        if r == c and leftDiagonal(check):
            count = count + 1
        if r + c == 4 and rightDiagonal(check):
            count = count + 1
        if count >= 3:
            print(i * 5 + j + 1)
            exit(0)
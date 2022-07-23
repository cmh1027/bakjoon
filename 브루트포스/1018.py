import sys
input = sys.stdin.readline
def repaintCount1(M, I, J): # 첫칸이 Black
    count = 0
    for i in range(I, I+8):
        for j in range(J, J+8):
            if (i + j) % 2 == 0 and M[i][j] == 'W':
                count += 1
            elif (i + j) % 2 == 1 and M[i][j] == 'B':
                count += 1
    return count

def repaintCount2(M, I, J): # 첫칸이 White
    count = 0
    for i in range(I, I+8):
        for j in range(J, J+8):
            if (i + j) % 2 == 0 and M[i][j] == 'B':
                count += 1
            elif (i + j) % 2 == 1 and M[i][j] == 'W':
                count += 1
    return count

M, N = map(int, input().split())
chessboard = []
for _ in range(M):
    chessboard.append(list(input().strip()))
minCount = float('inf')
for i in range(M-7):
    for j in range(N-7):
        minCount = min(minCount, min(repaintCount1(chessboard, i, j), repaintCount2(chessboard, i, j)))
print(minCount)

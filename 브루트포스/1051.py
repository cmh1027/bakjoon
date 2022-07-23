import sys
input = sys.stdin.readline
N, M = map(int, input().split())
minSquare = min(N, M)
L = []
maxSize = 0
for _ in range(N):
    L.append(list(map(int, list(input().strip()))))

def findSquare(i, j):
    global minSquare, N, M, L
    maxSquareSize = 0
    for S in range(minSquare):
        if i + S >= N or j + S >= M:
            break
        if L[i][j] == L[i+S][j] == L[i][j+S] == L[i+S][j+S]:
            maxSquareSize = max(maxSquareSize, (S+1)**2)
    return maxSquareSize

for i in range(N):
    for j in range(M):
        maxSize = max(maxSize, findSquare(i, j))
print(maxSize)
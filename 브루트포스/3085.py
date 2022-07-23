import sys
input = sys.stdin.readline
def countRowCandy(M, N, i):
    maxSequence = 0
    currentSequence = 0
    current = -1
    for j in range(N):
        if M[i][j] == current:
            currentSequence += 1
        else:
            if maxSequence < currentSequence:
                maxSequence = currentSequence
            current = M[i][j]
            currentSequence = 1
    if maxSequence < currentSequence:
        maxSequence = currentSequence
    return maxSequence

def countColCandy(M, N, j):
    maxSequence = 0
    currentSequence = 0
    current = -1
    for i in range(N):
        if M[i][j] == current:
            currentSequence += 1
        else:
            if maxSequence < currentSequence:
                maxSequence = currentSequence
            current = M[i][j]
            currentSequence = 1
    if maxSequence < currentSequence:
        maxSequence = currentSequence
    return maxSequence

N = int(input())
M = []
maxCandy = 1
for _ in range(N):
    M.append(list(input().strip()))
for i in range(N-1):
    for j in range(N):
        M[i][j], M[i+1][j] = M[i+1][j], M[i][j] # 위아래
        maxCandy = max(maxCandy, max(countRowCandy(M, N, i), countRowCandy(M, N, i+1)))
        maxCandy = max(maxCandy, countColCandy(M, N, j))
        M[i][j], M[i+1][j] = M[i+1][j], M[i][j] # 원위치
for i in range(N):
    for j in range(N-1):
        M[i][j], M[i][j+1] = M[i][j+1], M[i][j] # 좌우
        maxCandy = max(maxCandy, max(countColCandy(M, N, j), countColCandy(M, N, j+1)))
        maxCandy = max(maxCandy, countRowCandy(M, N, i))
        M[i][j], M[i][j+1] = M[i][j+1], M[i][j] # 원위치
print(maxCandy)
L = []
N = int(input())
for _ in range(N):
    L.append(list(input()))

def function1(L, N, i): # i번째 행에서 제일 긴 길이
    maxLength = 1 # 지금까지의 최대 길이
    sequence = 1 # 현재 알파벳의 길이
    current = None # 현재 알파벳
    for j in range(N):
        if current == L[i][j]:
            sequence += 1
        else:
            if maxLength < sequence: # maxLength update
                maxLength = sequence
            sequence = 1
            current = L[i][j]
    if maxLength < sequence: # maxLength update
        maxLength = sequence
    return maxLength


def function2(L, N, j): # j번째 열에서 제일 긴 길이
    maxLength = 1 # 지금까지의 최대 길이
    sequence = 1 # 현재 알파벳의 길이
    current = None # 현재 알파벳
    for i in range(N):
        if current == L[i][j]:
            sequence += 1
        else:
            if maxLength < sequence: # maxLength update
                maxLength = sequence
            sequence = 1
            current = L[i][j]
    if maxLength < sequence: # maxLength update
        maxLength = sequence
    return maxLength

MAX = 0
for i in range(N): # 가로 교환 (i, j) <-> (i, j+1)
    for j in range(N-1):
        L[i][j], L[i][j+1] = L[i][j+1], L[i][j] # 교환
        A = function1(L, N, i) # i번째 행에서 최대 길이
        B = function2(L, N, j) # j번째 열에서 최대 길이
        C = function2(L, N, j+1) # j+1번째 열에서 최대 길이
        MAX = max(MAX, max(max(A, B), C))
        L[i][j], L[i][j+1] = L[i][j+1], L[i][j] # 원상복귀
for i in range(N-1): # 세로 교환 (i, j) <-> (i+1, j)
    for j in range(N):
        L[i][j], L[i+1][j] = L[i+1][j], L[i][j] # 교환
        A = function1(L, N, i) # i번째 행에서 최대 길이
        B = function1(L, N, i+1) # j번째 열에서 최대 길이
        C = function2(L, N, j) # j+1번째 열에서 최대 길이
        MAX = max(MAX, max(max(A, B), C))
        L[i][j], L[i+1][j] = L[i+1][j], L[i][j] # 교환
print(MAX)
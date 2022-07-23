import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []
i, j = 0, 0
while i < N and j < M:
    if A[i] < B[j]:
        C.append(A[i])
        i = i + 1
    else:
        C.append(B[j])
        j = j + 1
if i == N:
    C.extend(B[j:])
else:
    C.extend(A[i:])
for i in C:
    print(i, end=" ")
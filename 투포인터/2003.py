import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
start, end = 0, 0
count = 0
S = A[start]
while start < N:
    if S == M:
        count = count + 1
    if S <= M:
        end = end + 1
        if end >= len(A):
            break
        S += A[end]
    else:
        S -= A[start]
        start = start + 1
print(count)
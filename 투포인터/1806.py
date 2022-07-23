import sys
input = sys.stdin.readline
N, S = map(int, input().split())
A = list(map(int, input().split()))
start, end = 0, 0
count = 0
minimum = float('inf')
X = A[start]
while start < N:
    if X >= S:
        if end - start + 1 < minimum:
            minimum = end - start + 1
    if X <= S:
        end = end + 1
        if end >= len(A):
            break
        X += A[end]
    else:
        X -= A[start]
        start = start + 1
if minimum == float('inf'):
    print(0)
else:
    print(minimum)
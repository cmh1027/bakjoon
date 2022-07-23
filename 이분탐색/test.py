import sys
input = sys.stdin.readline
def count(A, C):
    c = 0
    for i in A:
        c = c + i // C
    return c
K, N = map(int, input().split())
A = []
for _ in range(K):
    A.append(int(input()))
left = 1
right = max(A)
maxLength = 0
while left <= right:
    mid = (left + right) // 2
    c = count(A, mid)
    if K <= c: # 조건
        left = mid + 1
        if maxLength < mid:
            maxLength = mid
    else:
        right = mid - 1
print(maxLength)
import sys
input = sys.stdin.readline
N = int(input())
L = list(map(int, input().split()))
i = N-1
while i >= 1:
    if L[i-1] < L[i]:
        break
    i = i - 1
if i == 0:
    print(-1)
else:
    left, right = L[:i], L[i:]
    for i in range(len(right)-1, -1, -1):
        if left[-1] < right[i]:
            left[-1], right[i] = right[i], left[-1]
            right.sort()
            print(*(left+right))
            break
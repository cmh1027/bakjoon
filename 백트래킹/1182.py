import sys
input = sys.stdin.readline
N, S = map(int, input().split())
L = list(map(int, input().split()))
count = 0
def subset(i, subsum):
    global count, N, S, L
    if i >= N:
        return
    subset(i+1, subsum)
    subsum += L[i]
    if subsum == S:
        count += 1
    subset(i+1, subsum)

subset(0, 0)
print(count)
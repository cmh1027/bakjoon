import sys
import itertools
input = sys.stdin.readline
N, S = map(int, input().split())
L = list(map(int, input().split()))
count = 0
t = 0
# for i in range(1, N+1):
#     for t in itertools.combinations(L, i):
#         if sum(t) == S:
#             count += 1
# print(count)
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
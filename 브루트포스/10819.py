import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
L = list(map(int, input().split()))
m = 0
for p in permutations(L, N):
    s = 0
    for i in range(N-1):
        s += abs(p[i] - p[i+1])
    m = max(s, m)
print(m)
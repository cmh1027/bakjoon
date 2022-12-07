import sys
from itertools import combinations
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    A = list(map(int, input().split()))
    n, L = A[0], A[1:]
    S = 0
    for i, j in combinations(L, 2):
        S += math.gcd(i, j)
    print(S)
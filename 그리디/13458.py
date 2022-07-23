import sys
import math
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
number = N
for i in range(N):
    A[i] = A[i] - B if A[i] >= B else 0
    number += math.ceil(A[i] / C)
print(number)
import sys
from bisect import bisect_left, bisect_right
from collections import Counter
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
B = list(map(int, input().split()))
C = Counter(A) # dictionary
for value in B:
    print(C[value], end=" ")
# for value in B:
#     left = bisect_left(A, value)
#     right = bisect_right(A, value)
#     print(right - left, end=" ")



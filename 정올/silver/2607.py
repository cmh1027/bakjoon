import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
word = Counter(list(input().strip()))
count = 0
for _ in range(N-1):
    W = input().strip()
    A = Counter(list(W))
    X = sum((word - A).values())
    Y = sum((A - word).values()) 
    if X <= 1 and Y <= 1:
        count = count + 1
print(count)

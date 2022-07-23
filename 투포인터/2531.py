import sys
from collections import Counter
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))
if k == N:
    print(len(set(A)))
else:
    start, end = 0, k-1
    X = Counter(A[start:k] + [c])   
    maximum = len(X)
    while start < N:
        if A[start] != c:
            X[A[start]] -= 1
            if X[A[start]] == 0:
                del X[A[start]]
        start = start + 1
        end = (end+1) % N
        X[A[end]] += 1
        if maximum < len(X):
            maximum = len(X)
    print(maximum)
        


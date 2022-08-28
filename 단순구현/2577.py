import sys
input = sys.stdin.readline
A = int(input())
B = int(input())
C = int(input())
R = str(A*B*C)
L = [0] * 10
for c in R:
    L[int(c)] += 1
for i in L:
    print(i)
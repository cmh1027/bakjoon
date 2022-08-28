import sys
from collections import Counter
input = sys.stdin.readline
A = int(input())
B = int(input())
C = int(input())
result = Counter(list(str(A*B*C)))
for i in range(10):
    print(result[str(i)])
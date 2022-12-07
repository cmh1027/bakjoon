import sys
from collections import Counter
import math
input = sys.stdin.readline
S = input().strip()
C = Counter(S)
count = math.ceil((C['6'] + C['9']) / 2)
for key, value in C.items():
    if key == '6' or key == '9':
        continue
    count = max(count, value)
print(count)
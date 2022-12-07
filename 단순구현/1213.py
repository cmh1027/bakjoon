import sys
from collections import Counter
input = sys.stdin.readline
S = input().strip()
C = Counter(S)
odd = ""
for char, count in C.items():
    if count % 2 == 1:
        if odd == "" and len(S) % 2 == 1:
            odd = char
            C[char] -= 1
        else:
            print("I'm Sorry Hansoo")
            exit()
T = ""
for char, count in sorted(C.items()):
    T = T + char * (count // 2)
print(T + odd + T[::-1])
import sys
input = sys.stdin.readline
S = input().strip()
L = S.split('-')
for i in range(len(L)):
    L[i] = sum(map(int, L[i].split('+')))
print(L[0] - sum(L[1:]))
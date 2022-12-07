import sys
input = sys.stdin.readline
S = input().strip()
L = []
for y in range(len(S)):
    for x in range(1, y):
        A, B, C = S[:x], S[x:y], S[y:]
        L.append(A[::-1] + B[::-1] + C[::-1])
L.sort()
print(L[0])
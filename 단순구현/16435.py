import sys
input = sys.stdin.readline
N, L = map(int, input().split())
H = sorted(list(map(int, input().split())))
for i in H:
    if i <= L:
        L = L + 1
print(L)
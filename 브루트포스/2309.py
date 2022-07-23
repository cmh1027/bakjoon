import sys
input = sys.stdin.readline
L = []
for _ in range(9):
    L.append(int(input()))
S = sum(L)
for i in range(1, 9):
    for j in range(i):
        if L[i] + L[j] == S - 100:
            del L[i]
            del L[j]
            L.sort()
            for k in L:
                print(k)
            exit(0)
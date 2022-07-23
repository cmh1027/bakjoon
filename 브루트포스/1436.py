import sys
input = sys.stdin.readline
N = int(input())
L = []
i = 666
while True:
    if str(i).find("666") != -1:
        L.append(i)
    i = i + 1
    if len(L) == N:
        break
print(L[N-1])
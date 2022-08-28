import sys
input = sys.stdin.readline
L = []
for _ in range(10):
    L.append(int(input()) % 42)
print(len(set(L)))
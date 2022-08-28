import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    L = list(map(int, input().split()))
    L.sort()
    print(L[-3])
import sys
input = sys.stdin.readline
N = int(input())
length = len(str(N))
for i in range(max(0, N-9*length), N):
    if sum(map(int, str(i))) + i == N:
        print(i)
        exit(0)
print(0)
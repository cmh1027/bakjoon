import sys
input = sys.stdin.readline
N = int(input())
L = list(map(int, input().split()))
S = [0] * N
space = list(range(N))
for i in range(N):
    index = L[i]
    while S[index] != 0 or space[index] < L[i]:
        index = index + 1
    S[index] = i+1
    for j in range(index, N):
        space[j] -= 1
print(*S)
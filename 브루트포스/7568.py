import sys
input = sys.stdin.readline
N = int(input())
L = []
rank = []
for _ in range(N):
    x, y = map(int, input().split())
    L.append((x, y))
for i in range(N):
    count = 0
    for j in range(N):
        if i != j and L[i][0] < L[j][0] and L[i][1] < L[j][1]:
            count = count + 1
    rank.append(count+1)
print(*rank)

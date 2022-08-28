import sys
input = sys.stdin.readline
paper = [[0] * 100 for _ in range(100)]
N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    for i in range(A, A+10):
        for j in range(B, B+10):
            paper[i][j] = 1
print(sum(map(sum, paper)))
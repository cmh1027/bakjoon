import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
line = [1]
for i in range(1, N):
    pick = A[i]
    line.insert(len(line)-pick, i+1)
print(*line)
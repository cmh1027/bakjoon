import sys
input = sys.stdin.readline
odds = []
for i in range(7):
    N = int(input())
    if N % 2 == 1:
        odds.append(N)
if len(odds) == 0:
    print(-1)
else:
    print(sum(odds))
    print(min(odds))
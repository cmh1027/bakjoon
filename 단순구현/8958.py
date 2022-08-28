import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    S = input().strip()
    scoreSum = 0
    score = 0
    for c in S:
        if c == 'O':
            score += 1
            scoreSum += score
        else:
            score = 0
    print(scoreSum)
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    scores = []
    number = 0
    N = int(input())
    for _ in range(N):
        first, second = map(int, input().split())
        scores.append((first, second))
    scores = sorted(scores)
    top = float('inf')
    for first, second in scores:
        if top > second:
            top = second
            number += 1
    print(number)
import sys
input = sys.stdin.readline
N = int(input())
scores = []
for _ in range(N):
    A, B, C = map(int, input().split())
    if A != B and B != C and C != A:
        scores.append(max([A, B, C]) * 100)
    elif A == B == C:
        scores.append(10000 + 1000 * A)
    else:
        if A == B or A == C:
            scores.append(1000 + 100 * A)
        elif B == C:
            scores.append(1000 + 100 * B)
print(max(scores))
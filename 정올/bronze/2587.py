import sys
input = sys.stdin.readline
scores = []
for _ in range(5):
    scores.append(int(input()))
print(int(sum(scores) / len(scores)), sorted(scores)[2])
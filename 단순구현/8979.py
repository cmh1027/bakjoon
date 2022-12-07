import sys
input = sys.stdin.readline
N, K = map(int, input().split())
scores = []
for _ in range(N):
    scores.append(list(map(int, input().split()))) # num, gold, silver, iron
for i in range(N):
    num, gold, silver, iron = scores[i]
    scores[i] = (num, gold*(1000001**2)+silver*(1000001)+iron)
scores.sort(key=lambda x:x[1], reverse=True)
for i in range(N):
    if scores[i][0] == K:
        index = i
for i in range(N):
    if scores[i][1] == scores[index][1]:
        print(i+1)
        break
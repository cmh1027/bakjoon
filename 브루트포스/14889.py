import sys
from itertools import combinations, permutations
input = sys.stdin.readline
N = int(input())
L = []
for _ in range(N):
    L.append(list(map(int, input().split())))
minVal = float('inf')
groups = combinations(list(range(1, N+1)), N//2)
for startTeam in groups:
    startTeamScore, linkTeamScore = 0, 0
    linkTeam = []
    for i in range(1, N+1):
        if i not in startTeam:
            linkTeam.append(i)
    for i, j in combinations(startTeam, 2):
        startTeamScore += (L[i-1][j-1] + L[j-1][i-1])
    for i, j in combinations(linkTeam, 2):
        linkTeamScore += (L[i-1][j-1] + L[j-1][i-1])
    minVal = min(minVal, abs(startTeamScore - linkTeamScore))
print(minVal)
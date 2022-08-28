import sys
from itertools import combinations
input = sys.stdin.readline
while True:
    L = list(map(int, input().split()))
    if L[0] == 0:
        break
    k, S = L[0], L[1:]
    for c in combinations(S, 6):
        print(*c)
    print()

# def combinations(N, M):
#     perms = []
#     visited = [False] * (N+1)
#     def recursion(index, L):
#         if index == M:
#             perms.append(L)
#             return
#         for i in range(1 if L == [] else int(L[-1]), N+1):
#             if visited[i] is False:
#                 visited[i] = True
#                 recursion(index+1, L+[i])
#                 visited[i] = False
#     recursion(0, [])
#     return perms
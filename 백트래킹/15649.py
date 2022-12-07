import sys
input = sys.stdin.readline
N, M = map(int, input().split())
X = list(map(int, input().split()))
X.sort()
perms = []
visited = [False] * (N+1)
def recursion(index, L):
    if index == M:
        perms.append(L)
        return
    for i in range(N):
        if visited[i] is False:
            visited[i] = True
            recursion(index+1, L+[X[i]])
            visited[i] = False

recursion(0, [])
for c in perms:
    print(*c)

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
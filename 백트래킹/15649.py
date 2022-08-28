import sys
input = sys.stdin.readline
N, M = map(int, input().split())
# from itertools import permutations
# for c in permutations(range(1, N+1), M):
#     print(*c)
def permutations(N, M):
    perms = []
    visited = [False] * (N+1)
    def recursion(index, L):
        if index == M:
            perms.append(L)
            return
        for i in range(1, N+1):
            if visited[i] is False:
                visited[i] = True
                recursion(index+1, L+[i])
                visited[i] = False
    recursion(0, [])
    return perms
for c in permutations(N, M):
    print(*c)
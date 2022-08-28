import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lis = list(map(int, input().split()))
lis.sort()
# from itertools import itertools
# for c in itertools(L, M):
#     print(*c)
def permutations(M, lis):
    perms = []
    visited = set()
    def recursion(index, L):
        if index == M:
            perms.append(L)
            return
        for i in lis:
            if i not in visited:
                visited.add(i)
                recursion(index+1, L+[i])
                visited.remove(i)
    recursion(0, [])
    return perms
for c in permutations(M, lis):
    print(*c)
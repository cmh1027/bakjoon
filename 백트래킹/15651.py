import sys
input = sys.stdin.readline
N, M = map(int, input().split())
# from itertools import product
# for c in product(range(1, N+1), repeat=M):
#     print(*c)
perms = []
def recursion(index, L):
    if index == M:
        perms.append(L)
        return
    for i in range(1, N+1):
        recursion(index+1, L+[i])

recursion(0, [])
for c in perms:
    print(*c)
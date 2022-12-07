import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lis = list(map(int, input().split()))
lis.sort()
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

for c in perms:
    print(*c)
# pypy말고 python으로 제출하면 시간초과
import sys
input = sys.stdin.readline
N = int(input())
eggs = []
for _ in range(N):
    eggs.append(list(map(int, input().split())))
maximum = 0
broken = [False] * (N+1)
def recursion(index, brokenCount):
    global eggs, maximum, broken
    def hit(a, b):
        eggs[a][0] -= eggs[b][1]
        if eggs[a][0] <= 0:
            broken[a] = True
            return 1
        return 0
    def recover(a, b):
        eggs[a][0] += eggs[b][1]
        broken[a] = False   
    if index == N:
        return
    if broken[index] is True:
        recursion(index+1, brokenCount)
        return
    for i in range(N):
        if i != index and broken[i] is False:
            newBroken = hit(i, index) + hit(index, i)
            maximum = max(maximum, brokenCount + newBroken)
            recursion(index+1, brokenCount + newBroken)
            recover(index, i)  
            recover(i, index)
recursion(0, 0)
print(maximum)
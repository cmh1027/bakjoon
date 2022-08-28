# import sys
# input = sys.stdin.readline
# def distance(xs, ys, x, y):
#     dist = 0
#     for i, j in zip(xs, ys):
#         dist += abs(i - x) + abs(j - y)
#     return dist

# N, M = map(int, input().split())
# xs = []
# ys = []
# for _ in range(M):
#     x, y = map(int, input().split())
#     xs.append(x)
#     ys.append(y)
# xs.sort()
# ys.sort()
# print(distance(xs, ys, xs[(M-1)//2], ys[(M-1)//2]))
import sys
input=sys.stdin.readline
length,s=map(int,input().split())
xlis=[]
ylis=[]
for _ in range(s):
    x,y=map(int, input().split())
    xlis.append(x)
    ylis.append(y)
xlis.sort()
ylis.sort()
xmid=xlis[s//2]
ymid=ylis[s//2]
print(xmid, ymid)
d = 0
for i in range(s):
    d+=abs(xlis[i]-xmid)+abs(ylis[i]-ymid)
print(d) 
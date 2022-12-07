import sys
input=sys.stdin.readline
n=int(input())
l=[]
for _ in range(n):
    l.append(list(map(int, input().split())))
ze=[0]*3
ze[0],ze[1],ze[2]=l[0][0],l[0][1],l[0][2]
for i in range(1,n):
    ze[0], ze[1], ze[2] = l[i][0] + min(ze[1], ze[2]), l[i][1] + min(ze[0], ze[2]), l[i][2] + min(ze[0], ze[1])
print(min(ze)) 
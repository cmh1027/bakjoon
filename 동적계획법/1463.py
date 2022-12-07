import sys
input=sys.stdin.readline
n=int(input())
L=[0]*(n+1)
save=[-1]*(n+1)
if n >= 2:
    save[2], L[2] = 1, 1
if n >= 3:
    save[3], L[3] = 0, 1
for i in range(4,n+1):
    L[i]=L[i-1]+1
    save[i]=2
    if i%2==0:
        if L[i//2]+1<L[i]:
            save[i]=1
        L[i]=min(L[i],L[i//2]+1)
    if i%3==0:
        if L[i//3]+1<L[i]:
            save[i]=0
        L[i]=min(L[i],L[i//3]+1)
print(L[n])
x=n
while x>=1:
    print(x,end=' ')
    if save[x]==0:
        x=x//3
    elif save[x]==1:
        x=x//2
    else:
        x-=1 
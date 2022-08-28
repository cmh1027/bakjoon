import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    pri=[]
    x,y=input().split()
    words=list(y)
    for i in words:
        print(i * int(x), end='')
    print()
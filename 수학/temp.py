import sys
input=sys.stdin.readline
def func(N):
    L = [0] * (N+1) # 0 : 내가 이김 / 1 : 상대가 이김
    L[1] = 0
    L[2] = 0
    L[3] = 1
    for i in range(4, N+1):
        if L[i-1] == 0 and L[i-2] == 0 and L[i-4] == 0:
            L[i] = 1
        else:
            L[i] = 0
    if L[N] == 0:
        print("SK")
    else:
        print("CY")
for i in range(3, 31):
    func(i)
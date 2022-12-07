import sys
input = sys.stdin.readline
N = int(input())
L = [0, 0]
save = [-1, -1] 
# 0 : divide by 3
# 1 : divide by 2 
# 2 : minus 1
for i in range(2, N+1):
    L.append(L[i-1] + 1)
    save.append(2)
    if i % 2 == 0:
        if L[i//2]+1 < L[i]:
            save[i] = 1
        L[i] = min(L[i//2]+1, L[i])
    if i % 3 == 0:
        if L[i//3]+1 < L[i]:
            save[i] = 0
        L[i] = min(L[i//3]+1, L[i])
print(L[N])
i = N
while i >= 1:
    print(i, end=" ")
    if save[i] == 0:
        i = i // 3
    elif save[i] == 1:
        i = i // 2
    else:
        i = i - 1
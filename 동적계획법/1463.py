import sys
input = sys.stdin.readline
N = int(input())
L = [0] * (N+1)
L[1] = 0
for i in range(2, N+1):
    if i % 2 != 0 and i % 3 != 0:
        L[i] = L[i-1] + 1
    elif i % 2 == 0 and i % 3 != 0:
        L[i] = min(L[i-1], L[i//2]) + 1
    elif i % 2 != 0 and i % 3 == 0:
        L[i] = min(L[i-1], L[i//3]) + 1
    else:
        L[i] = min(L[i-1], min(L[i//2], L[i//3])) + 1
# for i in range(2, N+1):
#     L.append(L[i-1] + 1)
#     if i % 2 == 0:
#         L[i] = min(L[i//2]+1, L[i])
#     if i % 3 == 0:
#         L[i] = min(L[i//3]+1, L[i])
print(L[N])

# L[0] dummy
# L[1] = 0
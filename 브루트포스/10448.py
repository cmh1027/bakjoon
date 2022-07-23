import sys
input = sys.stdin.readline
def function(L, K):
    for i in range(len(L)):
        for j in range(len(L)):
            for k in range(len(L)):
                if K == L[i] + L[j] + L[k]:
                    return 1
    return 0
L = []
n = 1
while n * (n+1) // 2 <= 1000:
    L.append(n * (n+1)//2)
    n = n + 1
T = int(input())
for _ in range(T):
    K = int(input())
    print(function(L, K))

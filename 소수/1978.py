import sys
input = sys.stdin.readline
N = int(input())
L = list(map(int, input().split()))
M = max(L)
prime = [True] * (M+1)
prime[1] = False
for i in range(2, M+1):
    if prime[i] is True:
        for j in range(2*i, M+1, i):
            prime[j] = False
count = 0
for i in L:
    if prime[i] is True:
        count = count + 1
print(count)
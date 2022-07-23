import sys
input = sys.stdin.readline
N = int(input())
isPrime = [True] * (N+1)
prime = []
for i in range(2, N+1):
    if isPrime[i] is True:
        for j in range(2*i, N+1, i):
            isPrime[j] = False
for i in range(2, N+1):
    if isPrime[i] is True:
        prime.append(i)
if N == 1:
    print(0)
else:
    start, end = 0, 0
    count = 0
    S = prime[start]
    while start < N:
        if S == N:
            count = count + 1
        if S <= N:
            end = end + 1
            if end >= len(prime):
                break
            S += prime[end]
        else:
            S -= prime[start]
            start = start + 1
    print(count)
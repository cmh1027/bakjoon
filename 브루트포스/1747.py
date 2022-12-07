import sys
input = sys.stdin.readline
N = int(input())
isPrime = [True] * (1000001)
isPrime[1] = False
for i in range(2, 1000001):
    if isPrime[i] is True:
        x = i * 2
        while x < 1000000:
            isPrime[x] = False
            x = x + i
for i in range(N, 1000001):
    if isPrime[i] is False:
        continue
    S = str(i)
    if S == S[::-1]:
        print(i)
        break
else:
    print(1003001)

    

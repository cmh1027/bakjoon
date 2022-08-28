import sys
input = sys.stdin.readline
N, K = map(int, input().split())
count = 0
number = -1
for i in range(1, N//2+1):
    if N % i == 0:
        count = count + 1
        number = i
    if count == K:
        print(number)
        exit(0)
count = count + 1
number = N
if count == K:
    print(number)
else:
    print(0)
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
count = 0
check = [False] * (N+1)
for i in range(2, N+1):
    if check[i] is False:
        j = 1
        while i * j <= N:
            if check[i*j] is True:
                j = j + 1
                continue
            count = count + 1
            if count == K:
                print(i*j)
                exit()
            check[i*j] = True
            j = j + 1
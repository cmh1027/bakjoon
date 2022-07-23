import sys
input = sys.stdin.readline
N, K = map(int, input().split())
coins = []
count = 0
for _ in range(N):
    coins.append(int(input()))
while K > 0:
    while len(coins) > 0 and coins[-1] > K:
        del coins[-1]
    # K = K - coins[-1]
    # count = count + 1
    count = count + K // coins[-1]
    K = K - (K // coins[-1]) * coins[-1]
    
print(count)
    
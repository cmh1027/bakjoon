import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
if M > 0:
    broken = list(map(int, input().split()))
    minCount = abs(100-N)
    for channel in range(1000001): # if N == 500000, broken = [1,2,3,4,5]
        for n in str(channel):
            if int(n) in broken:
                break
        else:
            minCount = min(minCount, len(str(channel)) + abs(channel - N))
    print(minCount)
else:
    print(min(len(str(N)), abs(100-N)))
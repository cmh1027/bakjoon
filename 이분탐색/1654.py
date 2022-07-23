import sys
input = sys.stdin.readline
def count(cable, length):
    c = 0
    for i in cable:
        c = c + i // length
    return c
K, N = map(int, input().split())
cable = []
for _ in range(K):
    cable.append(int(input()))
maxCable = 1
left, right = 1, max(cable)
while left <= right:
    mid = (left + right) // 2
    if count(cable, mid) >= N:
        if maxCable < mid:
            maxCable = mid
        left = mid + 1
    else:
        right = mid - 1
print(maxCable)
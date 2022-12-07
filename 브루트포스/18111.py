import sys
input = sys.stdin.readline
N, M, B = map(int, input().split())
L = []
for _ in range(N):
    L.append(list(map(int, input().split())))
minTime = sys.maxsize
height = None
for floor in range(257):
    destroy = 0
    build = 0
    for i in range(N):
        for j in range(M):
            if L[i][j] > floor:
                destroy = destroy + L[i][j] - floor
            else:
                build = build + floor - L[i][j]
    if destroy + B >= build:
        if minTime >= destroy * 2 + build:
            minTime = destroy * 2 + build
            height = floor
print(minTime, height)
import sys
input = sys.stdin.readline
N = int(input())
L = []
for _ in range(N):
    L.append(list(map(int, input().split()))) # (index, height)
endIndex = max(map(lambda x:x[0], L))
height = [0] * (endIndex+1)
for index, h in L:
    height[index] = h
maxHeight = max(height)
maxHeightIndices = []
for index, h in enumerate(height):
    if h == maxHeight:
        maxHeightIndices.append(index)
minIndex = min(maxHeightIndices)
maxIndex = max(maxHeightIndices)
area = (maxIndex - minIndex + 1) * maxHeight
currentHeight = 0
for i in range(minIndex):
    if height[i] > currentHeight:
        currentHeight = height[i]
    area += currentHeight
currentHeight = 0
for i in reversed(range(maxIndex+1, endIndex+1)):
    if height[i] > currentHeight:
        currentHeight = height[i]
    area += currentHeight
print(area)
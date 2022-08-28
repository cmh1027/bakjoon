import sys
input = sys.stdin.readline
def increasing(L):
    maximum = 1
    current = 1
    prev = L[0]
    for i in range(1, len(L)):
        if L[i] >= prev:
            current = current + 1
            maximum = max(maximum, current)
        else:
            current = 1
        prev = L[i]
    return maximum

def decreasing(L):
    maximum = 1
    current = 1
    prev = L[0]
    for i in range(1, len(L)):
        if L[i] <= prev:
            current = current + 1
            maximum = max(maximum, current)
        else:
            current = 1
        prev = L[i]
    return maximum
N = int(input())
L = list(map(int, input().split()))
print(max(increasing(L), decreasing(L)))
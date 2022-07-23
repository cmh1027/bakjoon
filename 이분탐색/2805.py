import sys
def treeTotal(trees, cut):
    total = 0
    for tree in trees:
        if tree > cut:
            total += tree - cut
    return total
input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))
left, right = 0, max(trees)
maxChop = 0
while left <= right:
    mid = (left + right) // 2
    if treeTotal(trees, mid) >= M:
        if maxChop < mid:
            maxChop = mid
        left = mid + 1
    else:
        right = mid - 1
print(maxChop)
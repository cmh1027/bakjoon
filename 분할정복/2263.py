import sys
def recursion(inStart, inEnd, postStart, postEnd):
    global inorder, postorder, inorderIdx
    if inStart > inEnd or postStart > postEnd:
        return
    root = postorder[postEnd]
    print(root, end=" ")
    rootIdx = inorderIdx[root]
    leftSize = rootIdx - inStart
    recursion(inStart, rootIdx-1, postStart, postStart+leftSize-1)
    recursion(rootIdx+1, inEnd, postStart+leftSize, postEnd-1)
    

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
inorder = list(map(int, input().split()))
inorderIdx = [0 for _ in range(N+1)]
for i in range(N):
    inorderIdx[inorder[i]] = i
postorder = list(map(int, input().split()))
recursion(0, N-1, 0, N-1)
import sys
input = sys.stdin.readline
def binarySearch(L, value):
    left, right = 0, len(L)-1
    while left <= right:
        mid = (left + right) // 2
        if L[mid] == value:
            return True
        elif L[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return False


N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
B = list(map(int, input().split()))
for value in B:
    if binarySearch(A, value) is True:
        print(1)
    else:
        print(0)

# N = int(input())
# A = list(map(int, input().split()))
# A = set(A)
# M = int(input())
# B = list(map(int, input().split()))
# for value in B:
#     if value in A:
#         print(1)
#     else:
#         print(0)
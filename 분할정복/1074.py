import sys
def divide(minimum, row, col, N):
    if N == 2: 
        if row == 0 and col == 0:
            return minimum
        elif row == 0 and col == 1:
            return minimum + 1
        elif row == 1 and col == 0:
            return minimum + 2
        else:
            return minimum + 3
    else: # N > 2이므로 4조각으로 나눠주기
        d = (N//2)**2
        if 0 <= row < N//2 and 0 <= col < N//2: # 좌상단
            return divide(minimum, row, col, N//2)
        elif 0 <= row < N//2 and N//2 <= col < N: # 우상단
            return divide(minimum + 1 * d, row, col-N//2, N//2)
        elif N//2 <= row < N and 0 <= col < N//2: # 좌하단
            return divide(minimum + 2 * d, row-N//2, col, N//2)
        else: # 우하단
            return divide(minimum + 3 * d, row-N//2, col-N//2, N//2)

input = sys.stdin.readline
N, r, c = map(int, input().split())
print(divide(0, r, c, 2**N))

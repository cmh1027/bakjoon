import sys
input = sys.stdin.readline
N, M, r, c, K = map(int, input().split())
_map = []
for _ in range(N):
    _map.append(list(map(int, input().split())))
def isValidCoord(r, c):
    global N, M
    return 0 <= r < N and 0 <= c < M
def roll(top, left, front, i):
    if i == 1:
        return left, 7-top, front 
    elif i == 2:
        return 7-left, top, front
    elif i == 3:
        return front, left, 7-top
    else:
        return 7-front, left, top
move = [None, (0,1), (0,-1), (-1,0), (1,0)]
dice = [None, 0, 0, 0, 0, 0, 0]
top, left, front = 1, 4, 5
for i in map(int, input().split()):
    dr, dc = move[i]
    if isValidCoord(r+dr, c+dc) is False:
        continue
    r, c = r+dr, c+dc
    top, left, front = roll(top, left, front, i)
    if _map[r][c] == 0:
        _map[r][c] = dice[7-top]
    else:
        dice[7-top] = _map[r][c]
        _map[r][c] = 0
    print(dice[top])
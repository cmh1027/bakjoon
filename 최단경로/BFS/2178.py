import sys
def isValid(row, col, N, M):
    if row >= 0 and col >= 0 and row < N and col < M:
        return True
    else:
        return False 
input = sys.stdin.readline
N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, list(input().strip()))))
move = [(-1, 0), (0, -1), (1, 0), (0, 1)]
visited = [[False] * M for _ in range(N)] # N X M
# visited = []
# for _ in range(N):
#     L = []
#     for _ in range(M):
#         L.append(False)
#     visited.append(L)


queue = [((0, 0), 1)] # coord, distance
while len(queue) > 0:
    coord, distance = queue[0]
    queue = queue[1:]
    row, col = coord
    if row == N-1 and col == M-1: # end point
        print(distance)
        break
    if visited[row][col] is False:
        visited[row][col] = True
        for m in move: 
            drow, dcol = m
            row_move, col_move = row + drow, col + dcol 
            # row, col = 4, 5
            # m = (-1, 0) row_move = 3, col_move = 5
            # m = (0, -1) row_omve = 4, col_move = 4
            # m = (1, 0) row_move = 5, col_move = 5
            # m = (0, 1) row_move = 4, col_move = 6
            if isValid(row_move, col_move, N, M) is True and maze[row_move][col_move] == 1:
                queue.append(((row_move, col_move), distance+1))
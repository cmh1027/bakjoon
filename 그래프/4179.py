import sys
import copy
def validCoord(R, C, r, c):
    return r >= 0 and r < R and c >= 0 and c < C
input = sys.stdin.readline
R, C = map(int, input().split())
maze = []
jihoon = None
fires = []
for r in range(R):
    text = input().strip()
    c = text.find('J')
    if c != -1:
        jihoon = (r, c)
    c = text.find('F')
    index = 0
    while text.find('F', index) != -1:
        c = text.find('F', index)
        fires.append((r, c))
        index = c+1
    maze.append(list(text))
d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
fireTrack = copy.deepcopy(maze)
for fire in fires:
    fireTrack[fire[0]][fire[1]] = 0
fireTrack[jihoon[0]][jihoon[1]] = '.'
fireQueue = fires
jihoonTrack = copy.deepcopy(maze)
jihoonTrack[jihoon[0]][jihoon[1]] = 0
for fire in fires:
    jihoonTrack[fire[0]][fire[1]] = '.'
jihoonQueue = [jihoon]
T = 0
while len(jihoonQueue) > 0:
    while len(fireQueue) > 0:
        top = fireQueue[0]
        top_r, top_c = top
        time = fireTrack[top_r][top_c]
        if time > T:
            break
        fireQueue = fireQueue[1:]
        for dr, dc in d:
            r, c = top_r + dr, top_c + dc
            if validCoord(R, C, r, c) is True and fireTrack[r][c] == '.':
                fireTrack[r][c] = time + 1
                fireQueue.append((r, c))

    while len(jihoonQueue) > 0:
        top = jihoonQueue[0]
        top_r, top_c = top
        time = jihoonTrack[top_r][top_c]
        if time > T:
            break
        jihoonQueue = jihoonQueue[1:]
        for dr, dc in d:
            r, c = top_r + dr, top_c + dc
            if validCoord(R, C, r, c) is True and jihoonTrack[r][c] == '.' and (fireTrack[r][c] == '.' or time+1 < fireTrack[r][c]):
                jihoonTrack[r][c] = time + 1
                jihoonQueue.append((r, c))
            elif validCoord(R, C, r, c) is False:
                print(time+1)
                exit(0)
    T = T + 1
print("IMPOSSIBLE")

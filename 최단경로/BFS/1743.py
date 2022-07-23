import sys
input = sys.stdin.readline
N, M, K = map(int, input().split()) # row, col, trash count
trash = set()
for _ in range(K):
    r, c = map(int, input().split())
    trash.add((r,c))
maximum = 0
move = [(-1, 0), (1, 0), (0, -1), (0, 1)] # top, bottom, left, right
visited = set()
for sr, sc in trash: # start row, start column
    if (sr, sc) in visited:
        continue
    size = 0
    ############ BFS ############
    queue = [(sr, sc)]
    while len(queue) > 0:
        coord = queue[0]
        queue = queue[1:]
        r, c = coord
        if (r,c) not in visited:
            visited.add((r,c))
            size = size + 1
            for dr, dc in move:
                if (r+dr, c+dc) not in visited and (r+sdr, c+dc) in trash:
                    queue.append((r+dr, c+dc))
    ############################
    if maximum < size: # update maximum
        maximum = size
print(maximum)
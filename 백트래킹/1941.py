import sys
from itertools import combinations
input = sys.stdin.readline
L = []
for _ in range(5):
    L.append(list(input().strip()))
case = combinations([(i, j) for i in range(5) for j in range(5)], 7)
def dasomSuperior(C):
    global L
    return sum([L[i][j] == 'S' for i, j in C]) >= 4
def adjacent(x, y):
    r1, c1 = x
    r2, c2 = y
    if r1 == r2 and abs(c1-c2) == 1 or abs(r1-r2) == 1 and c1 == c2:
        return True
    return False
def connected(C):
    visited = set()
    graph = dict()
    for i, x in enumerate(C):
        if x not in graph:
            graph[x] = []
        for j, y in enumerate(C):
            if i != j and adjacent(x, y) is True:
                graph[x].append(y)
    queue = [C[0]]
    while len(queue) > 0:
        front, queue = queue[0], queue[1:]
        if front not in visited:
            visited.add(front)
            queue.extend(graph[front])
    return len(visited) == len(C)
print(sum([connected(C) is True and dasomSuperior(C) is True for C in case]))
import sys
input = sys.stdin.readline
N = int(input())
paper = []
white, blue = 0, 0
for _ in range(N):
    paper.append(list(map(int, input().split())))
def allSame(row, col, L):
    global paper
    V = paper[row][col]
    for i in range(row, row+L):
        for j in range(col, col+L):
            if paper[i][j] != V:
                return False, None
    return True, V

def func(row, col, L):
    global paper, white, blue
    same, color = allSame(row, col, L)
    if same is True:
        if color == 0:
            white += 1
        else:
            blue += 1
    else:
        func(row, col, L//2)
        func(row+L//2, col, L//2)
        func(row, col+L//2, L//2)
        func(row+L//2, col+L//2, L//2)
func(0, 0, N)
print(white)
print(blue)
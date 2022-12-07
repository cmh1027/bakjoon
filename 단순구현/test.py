import sys
input = sys.stdin.readline
L = []
for _ in range(19):
    L.append(list(map(int, input().split())))
def garo(L):
    for row in range(19):
        current = L[row][0]
        s_row, s_col = row, 0
        count = 0
        for col in range(19):
            if L[row][col] == 0:
                current = 0
                count = 0
            elif current == L[row][col]:
                count = count + 1
                if count == 5:
                    if col + 1 < 19 and L[row][col+1] != current or col + 1 == 19:
                        return current, s_row, s_col
            else:
                current = L[row][col]
                count = 1
                s_row, s_col = row, col
    return None

def sero(L):
    for col in range(19):
        current = L[0][col]
        s_row, s_col = 0, col
        count = 0
        for row in range(19):
            if L[row][col] == 0:
                current = 0
                count = 0
            elif current == L[row][col]:
                count = count + 1
                if count == 5:
                    if row + 1 < 19 and L[row+1][col] != current or row + 1 == 19:
                        return current, s_row, s_col
            else:
                current = L[row][col]
                count = 1
                s_row, s_col = row, col
    return None

def leftDiagonal(L):
    for col in range(19):
        row = 0
        current = L[row][col]
        s_row, s_col = row, col
        count = 0
        while 0 <= row < 19 and 0 <= col < 19:
            if L[row][col] == 0:
                current = 0
                count = 0
            elif current == L[row][col]:
                count = count + 1
                if count == 5:
                    if row + 1 < 19 and col + 1 < 19 and L[row+1][col+1] != current or row + 1 == 19 or col + 1 == 19:
                        return current, s_row, s_col
            else:
                current = L[row][col]
                count = 1
                s_row, s_col = row, col
            row, col = row + 1, col + 1
    for row in range(19):
        col = 0
        current = L[row][col]
        s_row, s_col = row, col
        count = 0
        while 0 <= row < 19 and 0 <= col < 19:
            if L[row][col] == 0:
                current = 0
                count = 0
            elif current == L[row][col]:
                count = count + 1
                if count == 5:
                    if row + 1 < 19 and col + 1 < 19 and L[row+1][col+1] != current or row + 1 == 19 or col + 1 == 19:
                        return current, s_row, s_col
            else:
                current = L[row][col]
                count = 1
                s_row, s_col = row, col
            row, col = row + 1, col + 1
    return None

def rightDiagonal(L):
    for col in range(19):
        row = 18
        current = L[row][col]
        s_row, s_col = row, col
        count = 0
        while 0 <= row < 19 and 0 <= col < 19:
            if L[row][col] == 0:
                current = 0
                count = 0
            elif current == L[row][col]:
                count = count + 1
                if count == 5:
                    if row - 1 >= 0 and col + 1 < 19 and L[row-1][col+1] != current or row == 0 or col + 1 == 19:
                        return current, s_row, s_col
            else:
                current = L[row][col]
                count = 1
                s_row, s_col = row, col
            row, col = row - 1, col + 1
    for row in range(19):
        col = 0
        current = L[row][col]
        s_row, s_col = row, col
        count = 0
        while 0 <= row < 19 and 0 <= col < 19:
            if L[row][col] == 0:
                current = 0
                count = 0
            elif current == L[row][col]:
                count = count + 1
                if count == 5:
                    if row - 1 >= 0 and col + 1 < 19 and L[row-1][col+1] != current or row == 0 or col + 1 == 19:
                        return current, s_row, s_col
            else:
                current = L[row][col]
                count = 1
                s_row, s_col = row, col
            row, col = row - 1, col + 1
    return None

funcs = [garo, sero, leftDiagonal, rightDiagonal]
for func in funcs:
    result = func(L)
    if result is not None:
        current, row, col = result
        print(current)
        print(row+1, col+1)
        break
else:
    print(0)
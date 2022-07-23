import sys
def diamondSearch(diamond, startRow, startCol, endRow, endCol):
    num = 0
    coord = []
    for diaRow, diaCol in diamond:
        if startRow <= diaRow <= endRow and startCol <= diaCol <= endCol:
            num = num + 1
            coord.append((diaRow, diaCol))
    return num, coord

def trashSearch(trash, startRow, startCol, endRow, endCol):
    num = 0
    coord = []
    for trashRow, trashCol in trash:
        if startRow <= trashRow <= endRow and startCol <= trashCol <= endCol:
            num = num + 1
            coord.append((trashRow, trashCol))
    return num, coord

def rowCheck(row, coord):
    for r, c in coord:
        if row == r:
            return False
    return True

def colCheck(col, coord):
    for r, c in coord:
        if col == c:
            return False
    return True

def garoSlice(startRow, startCol, endRow, endCol, diamond, trash):
    diamondNum, diamondCoord = diamondSearch(diamond, startRow, startCol, endRow, endCol)
    trashNum, trashCoord = trashSearch(trash, startRow, startCol, endRow, endCol)
    if diamondNum == 0:
        return 0
    elif diamondNum == 1 and trashNum == 0:
        return 1
    elif diamondNum > 1 and trashNum == 0:
        return 0
    used = set()
    result = 0
    for row, col in trashCoord:
        if row not in used and rowCheck(row, diamondCoord) is True:
            a = seroSlice(startRow, startCol, row-1, endCol, diamond, trash)
            b = seroSlice(row+1, startCol, endRow, endCol, diamond, trash)
            result += a * b
        used.add(row)
    return result



def seroSlice(startRow, startCol, endRow, endCol, diamond, trash):
    diamondNum, diamondCoord = diamondSearch(diamond, startRow, startCol, endRow, endCol)
    trashNum, trashCoord = trashSearch(trash, startRow, startCol, endRow, endCol)
    if diamondNum == 0:
        return 0
    elif diamondNum == 1 and trashNum == 0:
        return 1
    elif diamondNum > 1 and trashNum == 0:
        return 0
    used = set()
    result = 0
    for row, col in trashCoord:
        if col not in used and colCheck(col, diamondCoord) is True:
            a = garoSlice(startRow, startCol, endRow, col-1, diamond, trash)
            b = garoSlice(startRow, col+1, endRow, endCol, diamond, trash)
            result += a * b
        used.add(col)
    return result

    
input = sys.stdin.readline
N = int(input())
mat = []
diamond = []
trash = []
result = 0
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            trash.append((i, j))
        elif row[j] == 2:
            diamond.append((i, j))
result += garoSlice(0, 0, N-1, N-1, diamond, trash)
result += seroSlice(0, 0, N-1, N-1, diamond, trash)
if result == 0:
    print(-1)
else:
    print(result)
import sys
input = sys.stdin.readline
L = []
for _ in range(19):
    L.append(list(map(int, input().split())))

def isValid(x):
    return 0 <= x < 19

def isFive(L, stack, dr, dc):
    r, c = stack[0]
    current = L[r][c]
    if isValid(r-dr) and isValid(c-dc) and current == L[r-dr][c-dc]:
        return False
    r, c = stack[-1]
    if isValid(r+dr) and isValid(c+dc) and current == L[r+dr][c+dc]:
        return False
    return True

def check(L, mode): # mode : 0(garo), 1(sero), 2(left down), 3(right down)
    d = [(0, 1), (1, 0), (1, -1), (1, 1)]
    dr, dc = d[mode]
    R = list(range(19)) + [0] * 19 + list(range(19))
    C = [0] * 19 + list(range(19)) + [18] * 19
    for row, col in zip(R, C):
        stack = []
        current = L[row][col]
        while isValid(row) and isValid(col):
            if L[row][col] == 0 or L[row][col] != current:
                stack = []
                if L[row][col] != 0:
                    stack.append((row, col))
                current = L[row][col]
            elif current == L[row][col]:
                stack.append((row, col))
                if len(stack) == 5:
                    if isFive(L, stack, dr, dc):
                        return current, stack
            row, col = row + dr, col + dc
    return None

for mode in range(4):
    result = check(L, mode)
    if result is not None:
        current, stack = result
        stack.sort(key=lambda x:x[1])
        r, c = stack[0]
        print(current)
        print(r+1, c+1)
        break
else:
    print(0)
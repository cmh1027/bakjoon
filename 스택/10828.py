import sys
input = sys.stdin.readline
N = int(input())
stack = []
def push(X):
    global stack
    stack.append(X)
def pop():
    global stack
    if stack == []:
        return -1
    else:
        value = stack[-1]
        stack = stack[:-1]
        return value
def size():
    global stack
    return len(stack)
def empty():
    global stack
    return int(len(stack) == 0)
def top():
    global stack
    if stack == []:
        return -1
    else:
        return stack[-1]
for _ in range(N):
    S = input().strip()
    if S == "pop":
        print(pop())
    elif S == "size":
        print(size())
    elif S == "empty":
        print(empty())
    elif S == "top":
        print(top())
    else:
        t, value = S.split()
        push(value)
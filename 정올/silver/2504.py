import sys
input = sys.stdin.readline
S = input().strip()
stack = []
for i in S:
    if i == '(' or i == '[':
        stack = [i] + stack
    else:
        if len(stack) == 0: # ]
            print(0)
            exit(0)
        top, stack = stack[0], stack[1:]
        if not (i == ')' and top == '(' or i == ']' and top == '['):
            print(0)
            exit(0)
if len(stack) != 0: # ()[
    print(0)
    exit(0)
for i in S:
    if i == ')' or i == ']':
        value = 0
        while True:
            top, stack = stack[0], stack[1:]
            if top == '(' and i == ')':
                if value == 0:
                    stack = [2] + stack
                else:
                    stack = [value * 2] + stack
                break
            elif top == '[' and i == ']':
                if value == 0:
                    stack = [3] + stack
                else:
                    stack = [value * 3] + stack
                break
            else:
                value = value + top
    else:
        stack = [i] + stack
print(sum(stack))
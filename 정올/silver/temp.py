import sys
input = sys.stdin.readline
S = input().strip()
stack = []
try:
    for c in S:
        if c != ')' and c != ']':
            stack.append(c)
        else:
            if c == ')':
                top = stack[-1]
                if top == '(':
                    stack.pop()
                    stack.append(2)
                else:
                    value = 0
                    while stack[-1] != '(':
                        value += stack.pop()
                    stack.pop()
                    stack.append(value * 2)
            elif c == ']':
                top = stack[-1]
                if top == '[':
                    stack.pop()
                    stack.append(3)
                else:
                    value = 0
                    while stack[-1] != '[':
                        value += stack.pop()
                    stack.pop()
                    stack.append(value * 3)
    print(sum(stack))
except IndexError:
    print(0)
except TypeError:
    print(0)
while True:
    S = input()
    if S == '.':
        break
    stack = []
    for i in S:
        if i == '(' or i == '[':
            stack.append(i)
        if i == ')':
            if len(stack) == 0 or stack[-1] != '(':
                print('no')
                break
            else:
                stack.pop()
        if i == ']':
            if len(stack) == 0 or stack[-1] != '[':
                print('no')
                break
            else:
                stack.pop()
    else:
        if len(stack) == 0:
            print('yes')
        else:
            print('no')

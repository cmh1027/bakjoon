import sys
input = sys.stdin.readline
N = int(input())
L = input().strip().split()
result = []
visited = [False] * 10
def check(ineq, x, y):
    if ineq == '<':
        return x < y
    else:
        return x > y
def func(length, string):
    global N
    if length == N+1:
        result.append(string)
        return
    for i in range(10):
        if len(string) == 0 or visited[i] is False and check(L[length-1], int(string[-1]), i) is True:
            visited[i] = True
            func(length+1, string + str(i))
            visited[i] = False
func(0, "")
print(result[-1])
print(result[0])
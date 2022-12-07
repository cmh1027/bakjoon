import sys
input = sys.stdin.readline
N, e, w, n, s = map(int, input().split())
probability = {'e':e, 'w':w, 'n':n, 's':s}
direction = {'e':(0,1), 'w':(0,-1), 'n':(-1,0), 's':(1,0)}
coords = []
result = 0
def dfs(n, cur, prob):
    global result 
    if n != 0:
        for d in ['e', 'w', 'n', 's']:
            x, y = direction[d]
            cur_x, cur_y = cur
            move_prob = probability[d]         
            next = (cur_x+x, cur_y+y)
            if next not in coords: 
                coords.append(cur)
                dfs(n-1, next, prob * move_prob)
                coords.pop()
    else:
        result += prob
dfs(N, (0, 0), 1)
print(result / (100**N))
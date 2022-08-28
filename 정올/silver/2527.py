import sys
input = sys.stdin.readline
for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    g1, s1, g2, s2 = (p1-x1)/2, (q1-y1)/2, (p2-x2)/2, (q2-y2)/2
    cx1, cy1, cx2, cy2 = x1+g1, y1+s1, x2+g2, y2+s2
    if abs(cx1-cx2) == g1 + g2 and abs(cy1-cy2) == s1 + s2:
        print('c')
    elif abs(cx1-cx2) == g1 + g2 and abs(cy1-cy2) < s1 + s2 or abs(cx1-cx2) < g1 + g2 and abs(cy1-cy2) == s1 + s2:
        print('b')
    elif abs(cx1-cx2) > g1 + g2 or abs(cy1-cy2) > s1 + s2:
        print('d')
    else:
        print('a')
import sys
input = sys.stdin.readline
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
p = p + t % (2*w)
if p > w:
    p = w - (p - w)
q = q + t % (2*h)
if q > h:
    q = h - (q - h)
print(abs(p), abs(q))
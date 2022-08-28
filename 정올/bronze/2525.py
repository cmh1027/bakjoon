import sys
input = sys.stdin.readline
hour, minute = map(int, input().split())
current = hour * 60 + minute
current = (current + int(input())) % 1440
print(current // 60, current % 60)
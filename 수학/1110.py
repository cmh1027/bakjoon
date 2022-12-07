import sys
input = sys.stdin.readline
N = int(input())
def func(N):
    return (N % 10) * 10 + sum(map(int, list(str(N)))) % 10
number = func(N)
count = 1
while number != N:
    number = func(number)
    count += 1
print(count)

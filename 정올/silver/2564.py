import sys
def transform(direction, position):
    if direction == 1:
        return position
    elif direction == 2:
        return r + c + r - position
    elif direction == 3:
        return r + c + r + c - position
    else:
        return r + position
input = sys.stdin.readline
r, c = map(int, input().split())
N = int(input())
shops = []
distance = 0
for _ in range(N):
    direction, position = map(int, input().split())
    shops.append(transform(direction, position))
direction, position = map(int, input().split())
dongun = transform(direction, position)
for shop in shops:
    minimum, maximum = min(dongun, shop), max(dongun, shop)
    distance = distance + min(maximum - minimum, minimum + 2 * r + 2 * c - maximum)
print(distance)
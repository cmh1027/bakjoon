N = int(input())
ropes = []
for i in range(N):
    ropes.append(int(input()))
ropes = sorted(ropes, reverse=True)
for i in range(N):
    ropes[i] = ropes[i] * (i+1)
print(max(ropes))

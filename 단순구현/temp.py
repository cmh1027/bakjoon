X = [[[0] * 20 for _ in range(20)] for _ in range(20)]
def w(a, b, c):
    global X
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        if X[20][20][20] != 0:
            return X[20][20][20]
        else:
            X[20][20][20] = w(20, 20, 20)
            return X[20][20][20]
    if a < b < c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        return w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)

print(w(23, 15, 10))
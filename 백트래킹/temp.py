def recursion(L, N, idx, result):
    if len(result) == N:
        print(*result)
        return
    if idx == len(L):
        return
    result.append(L[idx])
    recursion(L, N, idx+1, result)
    result.pop()
    recursion(L, N, idx+1, result)

def permutation(L, N):
    recursion(L, N, 0, [])

A = [1,2,3]
permutation(A, 2) 
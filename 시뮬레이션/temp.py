# CP template Version 1.4
import os
import sys
import itertools
import collections
from functools import cmp_to_key
from itertools import product
from collections import deque, Counter
from math import log, log2, ceil, floor
import math
from heapq import heappush, heappop

DEBUG = False


def main(f = None):
    init(f)
    n, m = map(int, input().split())
    mat = [[int(i) for i in input().split()] for _ in range(n)]

    cpy = [i[:] for i in mat]

    virusSources = []
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 2:
                virusSources.append((i, j))

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    def virus(mat):
        for i, j in virusSources:
            dfs(mat, i, j)
        #parr(mat)
        #print()
        return countSafe(mat)
    
    def countSafe(mat):
        count = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    count += 1
        return count

    def dfs(mat, y, x):
        mat[y][x] = 2

        for i, j in zip(dx, dy):
            ni = y + i
            nj = x + j
            if 0 <= ni < n and 0 <= nj < m:
                if mat[ni][nj] == 0:
                    dfs(mat, ni, nj)

    global safeArea
    safeArea = 0

    def wall(wallCount, mat, i, j):
        global safeArea
        while i < n:
            while j < m:
                if mat[i][j] == 0:
                    mat[i][j] = 8 
                    if wallCount < 2:
                        wall(wallCount + 1, mat, i, j)
                    else:
                        cpy = [i[:] for i in mat]
                        safeArea = max(virus(cpy), safeArea)
                    mat[i][j] = 0
                j += 1
                if j == m:
                    j = 0
                    break
            i += 1

    wall(0, mat, 0, 0)

    print(safeArea)


def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input=sys.stdin.readline

def init(f = None):
    if os.path.exists("o"): sys.stdout = open("o", "w")
    if f is not None: setStdin(f)
    else:
        if len(sys.argv) == 1:
            if os.path.isfile("in/i"): setStdin("in/i")
            elif os.path.isfile("i"): setStdin("i")
        elif len(sys.argv) == 2: setStdin(sys.argv[1])
        else: assert False, "Too many sys.argv: %d" % len(sys.argv)


def dprint(*args):
    if DEBUG: print(*args)

def pfast(*args, end = "\n", sep=' '): sys.stdout.write(sep.join(map(str, args)) + end)

def parr(arr):
    for i in arr:
        print(i)


if __name__ == "__main__":
    main()
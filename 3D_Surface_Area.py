#!/bin/python3

import math
import os
import random
import re
import sys

def surfaceArea(A):
    surf = H*W*2

    def check(i,j):
        return A[x+i][y+j] if 0<=x+i<H and 0<=y+j<W

    xi = [0,0,1,-1]          # the coordinates around the given cube to check
    yi = [1,-1,0,0]

    for x in range(H):
        for y in range(W):
            for i,j in zip(xi,yi):
                area += max(0, A[x][y] - check(i,j))

    return area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()

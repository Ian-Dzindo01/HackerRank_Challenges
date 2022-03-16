#!/bin/python3

import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    dia1 = 0
    dia2 = 0
    for x in range(len(arr)):
        for y in range(len(arr)):
            if(x == y):
                dia1 += arr[x][y]

    cnt1 = 0
    cnt2 = len(arr) - 1
    for x in range(len(arr)):
        dia2 += arr[cnt1][cnt2]
        cnt1 += 1
        cnt2 -= 1

    res = abs(dia1 - dia2)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

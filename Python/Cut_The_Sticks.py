#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.


def cutTheSticks(arr):
    res = []
    while(True):
        res.append(len(arr))
        sm = min(arr, default=0)
        arr = [x - sm for x in arr]
        arr = [item for item in arr if item > 0]
        if len(arr) == 0:
            break

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

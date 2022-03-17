#!/bin/python3

import math
import os
import random
import re
import sys

def closestNumbers(arr):
    arr.sort()
    smallest = abs(arr[0] - arr[1])
    indices = []

    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i+1]) < smallest:
            smallest = abs(arr[i] - arr[i+1])

    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i+1]) == smallest:
            indices.append(arr[i])
            indices.append(arr[i+1])

    return indices

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

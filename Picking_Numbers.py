#!/bin/python3

import math
import os
import random
import re
import sys


def pickingNumbers(a):
    a.sort(reverse=True)
    lengths = []
    for i in range(len(a)):
        temp = []
        temp.append(a[i])
        for j in range(i, len(a)):
            if abs(a[i] - a[j]) <= 1:
                temp.append(a[j])

        lengths.append(len(temp))

    lengths.sort(reverse=True)
    return lengths[0] - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

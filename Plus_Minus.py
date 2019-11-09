#!/bin/python3

import math
import os
import random
import re
import sys


def plusMinus(arr):
    neg = 0
    pos = 0
    zer = 0
    for x in arr:
        if(x > 0):
            pos += 1
        elif(x < 0):
            neg += 1
        else:
            zer += 1

    print(pos / len(arr))
    print(neg / len(arr))
    print(zer / len(arr))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

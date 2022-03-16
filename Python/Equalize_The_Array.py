#!/bin/python3

import math
import os
import random
import re
import sys
import collections

def equalizeArray(arr):
    cnt = collections.Counter(arr)
    freqs = list(cnt.values())
    freqs.sort(reverse=True)
    print(freqs)
    return len(arr) - freqs[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def gemstones(arr):
    old_set = set
    for i in arr:
        old_set = old_set.intersection(set(i))

    return len(old_set)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

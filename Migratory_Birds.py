#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def most_common(lst):
    data = Counter(lst)
    return data


def migratoryBirds(arr):
    res = most_common(arr)
    highest = max(res.values())
    most_freq = []

    for key, value in res.items():
        if(value == highest):
            most_freq.append(key)

    return sorted(most_freq)[0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

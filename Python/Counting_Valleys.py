#!/bin/python3

import math
import os
import random
import re
import sys


def countingValleys(n, s):
    cnt = 0
    vals_count = 0
    s = str(s)
    for val in s:
        if val == 'U':
            cnt += 1
        elif val == 'D':
            cnt -= 1

        if cnt == 0 and val == 'U':
            vals_count += 1

    return vals_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

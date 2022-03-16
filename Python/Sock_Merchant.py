#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def sockMerchant(n, ar):
    freqs = Counter(ar)
    cnt = 0
    for x in list(freqs.values()):
        cnt += int(x / 2)

    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

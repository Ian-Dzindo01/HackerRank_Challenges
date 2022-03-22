#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def lonelyinteger(a):
    res = Counter(a)
    for key, val in res.items():
        if val%2 == 1:
            return key


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()

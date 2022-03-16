#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def repeatedString(s, n):
    numa = Counter(s)['a']
    n1 = n // len(s)
    res = numa*n1
    diff = n - len(s)*n1
    newstr = s[:diff]
    res += Counter(newstr)['a']
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

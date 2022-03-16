#!/bin/python3

import math
import os
import random
import re
import sys

def camelcase(s):
    cnt = 1
    for letter in s:
        if letter.isupper():
            cnt += 1

    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()

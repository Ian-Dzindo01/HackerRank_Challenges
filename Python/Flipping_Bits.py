#!/bin/python3

import math
import os
import random
import re
import sys

def flippingBits(s):
    s = '{:032b}'.format(s)
    s = s.replace('1', 't')
    s = s.replace('0', '1')
    s = s.replace('t', '0')
    s = int(s, 2)
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

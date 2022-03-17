#!/bin/python3

import math
import os
import random
import re
import sys

def twoStrings(s1, s2):
    return 'NO' if not list(set(s1).intersection(s2)) else 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# b is the string
# n is the length of the string
# g is the number of test cases
def happyLadybugs(b):
    bugs = Counter(b)
    for i,j in bugs.items():
        if i != '_' and j == 1:
            return "NO"

    if bugs["_"] > 0:
        return "YES"
    else:
        pair = 0
        for i in range(len(b)-1):
            if b[i] == b[i+1]:
                pair += 1
            elif pair > 0:
                    pair = 0
            else:
                return "NO"

    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()

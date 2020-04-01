#!/bin/python3

import math
import os
import random
import re
import sys

def alternatingCharacters(s):
    cnt = 0
    for i in range(len(s)-1):
        if s[i] == 'A' and s[i+1] != 'B':
            cnt += 1
        if s[i] == 'B' and s[i+1] != 'A':
            cnt += 1

    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()

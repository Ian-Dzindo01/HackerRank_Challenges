#!/bin/python3

import math
import os
import random
import re
import sys

def hackerrankInString(s):
    tmp = 0
    cnt = 0
    h = 'hackerrank'
    for i in range(len(h)):
        for j in range(tmp, len(s)):
            if h[i] == s[j]:
                cnt += 1
                tmp = j
                break

    if cnt == len(h):
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()

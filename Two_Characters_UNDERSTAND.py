#!/bin/python3

import math
import os
import random
import re
import sys

def alternate(s):
    maxnum = count = 0
    uni = list(set(s))     # extracts unique chars from the string

    for i in range(len(uni)):
        for j in range(i+1, len(uni)):
            l = [uni[i], uni[j]]

            if s.index(uni[i]) < s.index(uni[j]):
                ind = 0
            else:
                ind = 1


            for char in s:
                if char in l:
                    if char == l[ind]:
                        count += 1
                        ind = ind ^ 1
                    else:
                        count = 0
                        break

            maxnum = max(maxnum, count)
            count = 0

    return maxnum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()

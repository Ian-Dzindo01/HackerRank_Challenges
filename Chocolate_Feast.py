#!/bin/python3

import math
import os
import random
import re
import sys

def chocolateFeast(n, c, m):
    no = n/c           #3
    wrappers = no      #3
    while True:
        if wrappers//m < 1:
            return int(no)

        no += wrappers//m              # 3//2 = 1   no je ovde 4
        newwrappers = wrappers//m      # newwrappers = 1
        newwrappers += wrappers%m
        wrappers = newwrappers        # newwrappers = 2 => wrappers = 2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()

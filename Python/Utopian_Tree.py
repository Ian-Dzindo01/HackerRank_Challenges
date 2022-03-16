#!/bin/python3

import math
import os
import random
import re
import sys


def utopianTree(n):
    tree = 1
    for x in range(n):
        if x % 2 == 0:
            tree *= 2
        else:
            tree += 1

    return tree


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()

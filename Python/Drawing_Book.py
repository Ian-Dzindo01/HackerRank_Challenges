#!/bin/python3

import os
import sys


def pageCount(n, p):
    begdiff = p
    endiff = n - p
    if(begdiff > endiff):
        if(endiff != 1):
            return (int(endiff / 2))
        else:
            return 1
    else:
        return (int(begdiff / 2))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

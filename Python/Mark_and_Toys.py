#!/bin/python3

import math
import os
import random
import re
import sys

def maximumToys(prices, k):
    res = 0
    i = 0
    prices.sort()
    while(True):
        if res + prices[i] <= k:
            res += prices[i]
            i += 1
        else:
            return i

    return i


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()

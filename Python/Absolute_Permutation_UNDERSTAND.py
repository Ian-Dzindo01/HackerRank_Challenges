#!/bin/python3

import math
import os
import random
import re
import sys

def absolutePermutation(n,k):
    a = list(range(n+1))
    if k == 0:                          # simply return the list if k is 0
        return a[1:]

    if n%2 == 1:                        # you cannot do it if the number is odd, check it.
        return [-1]

    for i in range(1,n-k+1):
        if a[i] == a[i+k]-k:
            a[i], a[i+k] = a[i+k], a[i]

        elif abs(i - a[i]) != k:
            return [-1]

    for i in range(n-k+1,n+1):
        if abs(i - a[i]) != k:
            return [-1]

    return a[1:]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

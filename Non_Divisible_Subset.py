#!/bin/python3

import math
import os
import random
import re
import sys

# For any number K, the sum of 2 values (A & B) is evenly divisible by K if the sum of the remainders of A/K + B/K is K. Special case when a and b are divisible,
# giving a sum of 0. For any such remainder, there is 1 and only 1 other remainder value which will make a sum divisible by K.

def nonDivisibleSubset(k, s):
    remainder = [0]*k
    for i in s:
        remainder[i%k] += 1         # for each index we will have the int count of that particular remainder

    maxnum = 0
    maxnum += min(remainder[0],1)    # if we had more than one element with remainder 0 it will be divisible by k

    if k%2 == 0:
        maxnum += min(remainder[k//2], 1)    # we can only take one element from that index, because if we grab more they will be equal to k.

    for i in range(1, k//2 + 1):
        if i != k-i:
            maxnum += max(remainder[i], remainder[k-i])

    return maxnum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()

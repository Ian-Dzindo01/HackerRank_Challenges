# Subtract ascii codes in the symmetrical positions.
# First turn the string into an array of ASCII values.

#!/bin/python3

import math
import os
import random
import re
import sys

def isPalindrome(s):
    if (s == s[::-1]):
        return True
    return False

def theLoveLetterMystery(s):
    total = 0
    arr = [ord(c) for c in s]
    for i in range(len(s)//2):
        total += abs(arr[i] - arr[len(arr)-(1+i)])

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()


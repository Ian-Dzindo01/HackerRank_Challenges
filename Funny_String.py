#!/bin/python3

import math
import os
import random
import re
import sys

def funnyString(s):
    str2 = s[::-1]
    lst1 = []
    lst2 = []
    diffs1 = []
    diffs2 = []

    for i in range(len(s)):
        lst1.append(ord(s[i]))

    for i in range(len(str2)):
        lst2.append(ord(str2[i]))

    for i in range(len(lst1)-1):
        diffs1.append(abs(lst1[i] - lst1[i+1]))

    for i in range(len(lst2)-1):
        diffs2.append(abs(lst2[i] - lst2[i+1]))

    if diffs1 == diffs2:
        return 'Funny'
    else:
        return 'Not Funny'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()

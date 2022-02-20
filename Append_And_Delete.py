#!/bin/python3

import math
import os
import random
import re
import sys

def appendAndDelete(s, t, k):
    for ops in reversed(range(1, k + 1)):
        if s == t[:len(s)] and len(t) - len(s) == ops or len(s) == 0:
            break
        s = s[:-1]

    return("Yes" if len(t) - len(s) <= ops else "No")




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()

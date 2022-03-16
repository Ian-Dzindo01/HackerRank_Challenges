#!/bin/python3

import math
import os
import random
import re
import sys

def superReducedString(s):
    s = list(s)
    while(True):
        found = False
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s.pop(i+1)
                s.pop(i)
                found = True
                break

        if s == '' or found == False:
            break

    s = ''.join(s)

    if str(s) == '':
        return 'Empty String'
    else:
        return s




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()

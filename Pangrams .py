#!/bin/python3

import math
import os
import random
import re
import sys
import string

def pangrams(s):
    s = sorted(set(s.lower().replace(' ','')))

    alph = sorted(set(string.ascii_lowercase))

    return 'pangram' if s == alph else 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# if all fequencies are even then it can be a pangram or if all but one are even then it can also be a pangram
def gameOfThrones(s):
    t = True
    c = Counter(s)

    for value in c.values():
        if value%2 != 0 and t == False:
            return 'NO'
        elif value%2 != 0 and t == True:
            t = False

    return 'YES'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()

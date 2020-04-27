# First remove all the spaces from the string.
# Take the square root of the length, the lower number is the number of rows and the upper number is the number of columns.

#!/bin/python3

import math
import os
import random
import re
import sys

def encryption(s):
    res = ""
    s = s.replace(" ", "")
    n = math.sqrt(len(s))
    nrows = round(n)                             # if it rounded to the upper value, then you will not add 1 to number of columns

    if (nrows - n) < 0:
        ncols = nrows + 1
    else:
        ncols = nrows

    for i in range(nrows):
        for j in range(ncols):
            if(i+(ncols*j) < len(s)):
                res += s[i+(ncols*j)]
            else:
                continue

        res += ' '

    return res

str1 = "chillout"
print(encryption(str1))

# chillout

# chi
# llo
# ut

# this turns out to 2 rows and 3 columns



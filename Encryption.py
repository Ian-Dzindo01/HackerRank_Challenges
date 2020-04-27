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
    n = math.sqrt(len(s))
    nrows = round(n)
    ncols = lower + 1
    s.replace(" ", "")




res = ""
str1 = 'ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots'
nrows = 7
ncols = 8
for i in range(nrows):
    for j in range(ncols):
        if(i+(8*j) < len(str1)):
            res += str1[i+(8*j)]
        else:
            continue

    res += ' '

print(res)




print(str1[8])

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = encryption(s)

#     fptr.write(result + '\n')

#     fptr.close()

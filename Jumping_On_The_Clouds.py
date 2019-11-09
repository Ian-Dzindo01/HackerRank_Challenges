# e = 100
# array of clouds c
# every jump costs 1 energy point
# jump of size k to cloud c[(i + k)%n].
# if she lands on c[i] = 1, her energy decreases by 2
# Game ends when she lands back on cloud 0
#!/bin/python3

import math
import os
import random
import re
import sys

# c is array of clouds, k is the size of the jump
def jumpingOnClouds(c, k):
    e = 100
    i = 0
    cc = c[i]
    n = len(c)
    while True:
        e -= 1
        i = (i + k)%n
        if c[i] == 1:
            e -= 2

        if i == 0:
            break

    return e

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()

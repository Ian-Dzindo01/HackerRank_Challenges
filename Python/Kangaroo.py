#!/bin/python3

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    jump_locs1 = [x1]
    jump_locs2 = [x2]
    for x in range(10000):
        jump_locs1.append(jump_locs1[x] + v1)
        jump_locs2.append(jump_locs2[x] + v2)

    for x in range(10000):
        if(jump_locs1[x] == jump_locs2[x]):
            return 'YES'

    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

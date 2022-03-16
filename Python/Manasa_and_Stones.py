# Try to figure out a repeating pattern in the results.
#!/bin/python3

import math
import os
import random
import re
import sys


def stones(n, a, b):
    result = set()
    if a > b:
        a,b = b,a

    for i in range(n):
        result.add(i*a + (n - 1 - i) * b)


    return sorted(list(result))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

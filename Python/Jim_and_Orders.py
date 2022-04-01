#!/bin/python3

import math
import os
import random
import re
import sys

def jimOrders(orders):
    d = {}
    for i in range(len(orders)):
        d[i+1] = orders[i][0] + orders[i][1]

    d = dict(sorted(d.items(), key=lambda item: item[1]))

    return list(d.keys())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

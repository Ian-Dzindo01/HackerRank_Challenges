#!/bin/python3

import math
import os
import random
import re
import sys


def countApplesAndOranges(s, t, a, b, apples, oranges):
    newapple = [x + a for x in apples]
    neworange = [x + b for x in oranges]
    cnta = 0
    cnto = 0
    for x in newapple:
        if x >= s and x <= t:
            cnta += 1

    for x in neworange:
        if x >= s and x <= t:
            cnto += 1

    print(cnta)
    print(cnto)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

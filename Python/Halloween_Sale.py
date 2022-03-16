#!/bin/python3

import math
import os
import random
import re
import sys

# p - game price
# d - every subsequent game costs this much less than the previous one
# m - d reduction continues until the price is lesser than or equal to this
# s - how much money you have

def howManyGames(p, d, m, s):
    games = 0
    while(True):
        s -= p
        p -= d

        if p <= m:
            p = m
            d = 0

        games += 1

        if s == 0:
            return games

        elif s < 0:
            return games - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()

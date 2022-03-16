#!/bin/python3

import math
import os
import random
import re
import sys

def climbingLeaderboard(ranked, player):
    ranks = []
    l = sorted(ranked + player, reverse=True)
    for i in range(len(l)):
        if l[i] == l[i-1] and i != 0:
            ranks[i] = i-1
            continue

        ranks[i] = i

    return [ranks[l.index(i)] for i in player]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


# I don't think the assignment is set up correctly.

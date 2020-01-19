#!/bin/python3

import math
import os
import random
import re
import sys

def cavityMap(grid):
    grid = list(map(str,grid))
    for i in range(len(grid)):
        for j in range(1, len(i)):
            if grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i][j+1]:
                grid[i][j] = 'X'

    return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

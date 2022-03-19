# This one times out. Will have to look for another way. Maybe use Binary Index Trees.
# If you have n intersections, you need to do n shifts to sort the list.
# If we are able to find the number of intersections, we will be able to find the nubmer of shifts that we need.
# If i < j and A[i] > A[j], then this is an arc or an inversion.
# You are also going to have to implement merge sort in order for this to work.

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

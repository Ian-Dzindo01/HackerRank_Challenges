#!/bin/python3

import math
import os
import random
import re
import sys

def workbook(n,k,a):

    num_special=0
    cur_page=1

    for i in range(len(a)):           #Iterates over the length of each chapter.

        num_probs_in_chapter=a[i]            #Number of problems in each chapter.
        num_full_pages, leftover_probs = divmod(num_probs_in_chapter, k)

        total_pages = num_full_pages + ( 1 if leftover_probs else 0 )
        problems_in_chapter=iter(range(1, a[i]+1))         #Iterable for problems in chapter

        for _ in range(total_pages):
            probs_on_page = [next(problems_in_chapter, None) for _ in range(k)]   #Stores the numbers of the problems on each page
            if cur_page in probs_on_page:
                num_special+=1
            cur_page+=1

    return num_special

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

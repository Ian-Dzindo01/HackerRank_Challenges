# count total number of letters and subtract each common element finding from the result
# return -1 if there is nothing that can be done
# def angrams(s):
#     cnt = len(s)
#     if len(s)%2 != 0:
#         return -1

#     s1 = s[:len(s)//2]
#     s2 = s[len(s)//2:]



# s = 'fdhlvosf pafhalll'
# res = angrams(s)
# print(res)


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#Solution taken from Hackers Realm on YouTube. Spent too much time on the problem. Nice and elegant solution. Feel stupid that I have not managed to implement
# this on my own.
def anagram(s):
    n = len(s)

    if n%2 == 1:
        return -1

    s = Counter(s[:n//2]) - Counter(s[n//2:])

    return sum(s.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()

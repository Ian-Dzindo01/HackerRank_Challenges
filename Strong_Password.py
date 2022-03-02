#!/bin/python3

import math
import os
import random
import re
import sys

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

def minimumNumber(n,password):
    if len(password) == 1:
        return 5

    if len(password) == 2:
        return 4

    if len(password) == 3:
        return 3

    num, low, up, spec = (False,)*4
    for i in password:
        if i in numbers:
            num = True
        elif i in lower_case:
            low = True
        elif i in upper_case:
            up = True
        elif i in special_characters:
            spec = True

    res =  [num,low,up,spec].count(False)
    if len(password) + res < 6:
        res += 6 - (len(password) + res)

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()

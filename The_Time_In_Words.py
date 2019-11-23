#!/bin/python3

import math
import os
import random
import re
import sys

num2words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'quarter', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
            19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two', \
            23: 'twenty three', 24: 'twenty four', 25: 'twenty five', 26: 'twenty six', \
            27: 'twenty seven', 28:'twenty eight', 29:'twenty nine', 0: 'zero'}

def timeInWords(h, m):
    if int(m) == 0:
        return num2words[h] + " o' clock"

    elif int(m) == 30:
        return "half past " + str(num2words[h])

    elif int(m) < 30:
        if int(m) == 1:
            return str(num2words[m]) + " minute past " + str(num2words[h])
        elif int(m) == 15:
            return str(num2words[m]) + " past " + str(num2words[h])
        else:
            return str(num2words[m]) + " minutes past " + str(num2words[h])

    else:
        temp = 60 - int(m)
        if temp == 1:
            return str(num2words[temp]) + " minute to " + str(num2words[h + 1])
        elif temp == 15:
            return str(num2words[temp]) + " to " + str(num2words[h + 1])
        else:
            return str(num2words[temp]) + " minutes to " + str(num2words[h + 1])

h = 6
m = 35

result = timeInWords(h, m)
print(result)

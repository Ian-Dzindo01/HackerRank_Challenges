#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

counts = Counter(input())     # counts frequency of each number in the first input string

#for key, value in counts.items():
#    print(key, value)

counts.subtract(input())  #substracts the values from the of the 2nd string from the 1st string

print(sum(abs(x) for x in counts.values()))    # sums up all of the remaining values in the counter

#!/bin/python3

import math
import os
import random
import re
import sys


s = input()
sm = s.replace(" ","")             # remove all spaces from string
r = math.floor(math.sqrt(len(sm)))     # number of rows
c = math.ceil(math.sqrt(len(sm)))      # number of columns

for i in range(c):
    print(sm[i::c],end=" ")     # takes the first value of every row, prints it and appends a space at the end of each word

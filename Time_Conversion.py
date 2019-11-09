#!/bin/python3

import os
import sys
from datetime import *


def timeConversion(s):
    return str(datetime.strptime(s, '%I:%M:%S%p'))[11:]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

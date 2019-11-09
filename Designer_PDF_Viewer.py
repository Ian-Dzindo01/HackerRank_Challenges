#!/bin/python3

import math
import os
import random
import re
import sys


def designerPdfViewer(word, hDict):
    hlist = []
    for x in word:
        hlist.append(heightDict[x])

    maxHeight = max(hlist)
    return maxHeight * len(word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    heightDict = dict(zip(alphabet, h))

    result = designerPdfViewer(word, heightDict)

    fptr.write(str(result) + '\n')

    fptr.close()

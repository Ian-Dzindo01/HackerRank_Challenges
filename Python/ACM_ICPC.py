import math
import os
import random
import re
import sys

# iterate through two strings simultaneously and see if there is a 1
# store the results in a dictionary
# we can also perform bitwise or operation
def acmTeam(topic):
    maxsub = 0
    count = 0

    for i in range(n):
        for j in range(i, n):
            sub = 0
            for x,y in zip(topic[i], topic[j]):
                if x == '1' or y == '1':
                    sub += 1

            if sub > maxsub:
                maxsub = sub
                count = 1
            elif sub == maxsub:
                count += 1

    return [maxsub, count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

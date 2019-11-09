#!/bin/python3

import os
import sys


def gradingStudents(grades):
    result = []
    for x in range(len(grades)):
        if(grades[x] > 37):
            if((grades[x] % 5) > 2):
                result.append(grades[x] + 5 - (grades[x] % 5))
            else:
                result.append(grades[x])
        else:
            result.append(grades[x])

    return result

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()

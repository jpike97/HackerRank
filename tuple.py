#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alicePoints = 0
    bobPoints = 0
    pointArr = []
    for x in range(0,3):
        if a[x] < b[x]:
            bobPoints += 1
        elif a[x] > b[x]:
            alicePoints += 1
    pointArr.append(alicePoints)
    pointArr.append(bobPoints)
    return pointArr
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

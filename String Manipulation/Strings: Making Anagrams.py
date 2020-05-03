#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    c = 0
    i = 0

    while(i<len(b)):
        if b[i] in a:
            r = b[i]
            a = a.replace(r, '', 1)
            b = b[:i]+b[i+1:]
            c = c+1
            
        elif b[i] not in a:
            i = i+1 

    val = len(a)+len(b)

    return val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
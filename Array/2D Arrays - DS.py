#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    li=[]
    for i in range(4):
        for j in range(4):
            val = arr[i][j+1] + arr[i][j] + arr[i][j+2] + arr[i+2][j+1] + arr[i+2][j] + arr[i+2][j+2] + arr[i+1][j+1]
            li.append(val)

    res=max(li)

    return res
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
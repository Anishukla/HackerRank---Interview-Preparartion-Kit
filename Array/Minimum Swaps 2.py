#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(A, N):
    swap = 0
    i = 0
    while(i<N):
        if A[i]!=i+1:
            val = A[i]
            A[val-1], A[i] = A[i], A[val-1]
            swap = swap+1
        
        elif A[i]==(i+1):
            i = i+1 

    return swap
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr, n)

    fptr.write(str(res) + '\n')

    fptr.close()


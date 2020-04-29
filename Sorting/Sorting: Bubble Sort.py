import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    count = 0
    for j in range(n):
        val = 0
        for i in range(1, n):
            if a[i-1] > a[i]:
                temp = a[i]
                a[i] = a[i-1]
                a[i-1] = temp
                count = count+1
            
            else:
                val = val+1
            
            if val == n-1:
                break
    return count

if __name__ == '__main__':
    n = int(input())
    temp = 0
    a = list(map(int, input().rstrip().split()))

    print("Array is sorted in", countSwaps(a), "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[n-1])
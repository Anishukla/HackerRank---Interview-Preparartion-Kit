 #!/bin/python3

import math
import os
import random
import re
import sys
from bisect import insort, bisect_right

def maximumSum(a, m):
    prefix = [0] * len(a)
    curr = 0;
    for i in range(len(a)):
        curr = (a[i] % m + curr) % m
        prefix[i] = curr
    
    pq = [prefix[0]]
    maxmodsum = max(prefix)
    for i in range(1, len(a)):
        left = bisect_right(pq, prefix[i])
        if left != len(pq):
            modsum = (prefix[i] - pq[left] + m) % m
            maxmodsum = max(maxmodsum, modsum)

        insort(pq, prefix[i])

    return maxmodsum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()


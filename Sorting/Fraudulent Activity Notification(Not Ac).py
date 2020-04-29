# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

import bisect

nd = input().split()
N = int(nd[0])
d = int(nd[1])
A = list(map(int, input().split()))

count = 0
val = []

for k in range(d):
    val.append(A[k])
    
val = sorted(val)

if d%2 == 1:
    req = val[int(d/2)]

elif d%2 == 0:
    req = (val[int(d/2)-1] + val[int(d/2)])/2
    
print(A[d], 2*req)
    
if A[d] >= 2*req:
    count = count+1

for i in range(d, N-1):
    req = 0
    
    val.remove(A[i-d])
    
    bisect.insort(val, A[i]) 

    if d%2 == 1:
        req = val[int(d/2)]

    elif d%2 == 0:
        req = (val[int(d/2)-1] + val[int(d/2)])/2
    
    if A[i+1] >= 2*req:
        count = count+1
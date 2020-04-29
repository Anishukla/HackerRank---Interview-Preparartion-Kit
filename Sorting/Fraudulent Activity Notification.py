# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

nd = input().split()
N = int(nd[0])
d = int(nd[1])
A = list(map(int, input().split()))

req =  [0]*201
res = 0

end = d
current = 0

for i in range(d):
    req[A[i]] = req[A[i]]+1
    
if d%2 == 0:
    mid = int(d/2)
    
else:
    mid = int(d/2)+1
    
while end < N:
    count, left = 0, 0
    
    while count<mid:
        count = count+req[left]
        left = left+1
        
    if count>mid or d%2 != 0:
        val = left-1
    
    else:
        val = left
        while req[left]==0:
            left = left+1
            
        val = val+left
    
    if A[end] >= val*2:
        res = res+1
        print(A[end])
        
    req[A[current]] = req[A[current]]-1
    req[A[end]] = req[A[end]]+1
    current = current+1
    end = end+1
    
print(res)


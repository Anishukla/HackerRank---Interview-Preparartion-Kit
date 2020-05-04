# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

"""
Finding the indexes such that the sum is K of 2 numbers in an array.
The solution uses mapping and making value already present key and its index
as the value finding y which is required value - current value of array element 
and if it's already present then printing it.

Time Complexity :- O(n) 

"""

T = int(input())

for i in range(T):
    req = int(input())
    N = int(input())
    
    A = list(map(int, input().split()))
    
    di = dict()
    
    for i in range(N):
        y = req-A[i]
        
        if y in di:
            print(di[y], i+1)
            break
        
        if y not in di:
            di.update({A[i]:i+1})
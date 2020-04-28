# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

T = int(input())

for i in range(T):
    N = int(input())   
    a = list(map(int, input().split()))
    
    val = 0
    x = 0
    res=0
    k = 0
    
    for i in range(N-1, -1,-1):
        
        if a[i]-(i+1)>2:
            k = 1
            print("Too chaotic")
            break
        
        for j in range(max(0, a[i] - 2), i):
            if a[j]>a[i]:
                res=res+1
    
    if k==0:          
        print(res)
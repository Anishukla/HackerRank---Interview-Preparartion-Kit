# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

n, m = input().split()
n = int(n)
d = int(m)

a = list(map(int, input().split()))
    
for i in range(d):
    val = a[0]
    a.remove(a[0])
    a.append(val)
    
    print(a)
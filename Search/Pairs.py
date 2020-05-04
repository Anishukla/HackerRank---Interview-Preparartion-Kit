# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

N, K = input().split()

N = int(N)
K = int(K)

A = list(map(int, input().split()))

d = {}
answer = 0
for i in A:
    d[i] = i

for j in A:
    g = j+K
    if g in d:
        answer = answer+1
            
print(answer)
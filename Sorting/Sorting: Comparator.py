# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

N = int(input())
class_list = dict()

for i in range(N):
    key, value = input().split()
    class_list[key] = int(value)
    
class_list = sorted(class_list.items(), key=lambda kv: (-kv[1], kv[0]))


for i in range(N):
    print(class_list[i][0], class_list[i][1])
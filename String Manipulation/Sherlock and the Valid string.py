# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

s = input()

l = len(s)
di = dict()
c = 0
for i in range(l):
    if s[i] not in di:
        di.update({s[i]:1})
    
    elif s[i] in di:
        di[s[i]] = di[s[i]]+1
        

li = list(di.values())

val = min(li)
val2 = max(li)

r1 = 0
r2 = 0

if val == 1 and val2>2:
    for i in range(len(li)):
        if li[i]==val:
            r1 = r1+1
        
        if li[i]==val2:
            r2 = r2+1
            
    if (r1+r2==len(li) and r2==len(li)-1):
        print("YES")
        
    else:
        print("NO")

else:
    for i in range(len(li)):
        if li[i]==val+1:
            r1 = r1+1
        
        if li[i]==val:
            r2 = r2+1
            
    if (r1+r2==len(li) and (r1>=len(li)-1 or r2>=len(li)-1)):
        print("YES")
        
    else:
        print("NO")
    
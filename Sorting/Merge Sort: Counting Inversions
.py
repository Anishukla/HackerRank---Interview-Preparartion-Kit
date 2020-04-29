# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

def merge(a,n1,index1,n2,index2,b,index,count):
    while n1!=0 and n2!=0:
        if a[index1]<=a[index2]:
            b[index]=a[index1]
            index+=1
            index1+=1
            n1-=1
        else:
            b[index]=a[index2]
            index+=1
            index2+=1
            n2-=1
            count+=n1
    while n1!=0:
        b[index]=a[index1]
        index+=1
        index1+=1
        n1-=1
    while n2!=0:
        b[index]=a[index2]
        index+=1
        index2+=1
        n2-=1
    return count,b

def mergepass(a,n,l,b,count):
    q=int(n/(2*l))   # total no. of pairs present
    s=2*l*q            # total no. of elements that are in pairs
    r=n-s                 #total no. of elements remaining without making any pair
    for i in range(q):
        lb=2*i*l        #lowerbound
        count,b = merge(a,l,lb,l,lb+l,b,lb,count)
    if r<=l:
        for i in range(r):
            b[s+i]=a[s+i]
    else:
        count,b = merge(a,l,s,r-l,s+l,b,s,count)
    return count,b

def countInversions(a,n):
    l=1
    count=0
    while l<n:
        b=[0]*n
        count,b=mergepass(a,n,l,b,count)
        a=[0]*n
        count,a=mergepass(b,n,l*2,a,count)
        l=4*l
    return count


T = int(input())

for i in range(T):
    n = int(input())

    arr = list(map(int, input().split()))

    result = countInversions(arr, n)

    print(result)
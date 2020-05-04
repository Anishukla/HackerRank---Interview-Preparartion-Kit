# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

""" Binary Search is used to solve this problem we first calculate
the lowe range and the upper range which are start and end and we know 
our answer must lie between the two so we do a binary search meanwhile 
calculating a value and when that value hits the goal and start<end that
is the minumum time in which goal can be achieved """

n, goal = input().split()
n = int(n)
goal = int(goal)

machines = list(map(int, input().split()))

req = max(machines)
req2 = min(machines)
start = int(goal//(len(machines)/req2))
end = int(goal//(len(machines)/req)) + 1
val = 0

while(start<end):
    check = (start+end)//2
    val = 0
    for i in range(n):
        val = val + int(check/machines[i])
        
    if val>=goal:
        end = (start+end)//2
        
    elif val<goal:
        start = (start+end)//2 +1
        
print(start)
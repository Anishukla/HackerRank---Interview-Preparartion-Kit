#Method 1(will give tle)
n, m = input().split()
n = int(n)
m = int(m)
queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

Li = [0]*n
for j in range(m):
    a = queries[j][0] - 1
    b = queries[j][1] - 1
    c = queries[j][2]
    
    for k in range(a, b+1):
        Li[k] = Li[k] + c
        

res = max(Li)

print(res)




#Method 2(AC)
n, m = input().split()
n = int(n)
m = int(m)
queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

Li = [0]*n
for j in range(m):
    a = queries[j][0] - 1
    b = queries[j][1]
    c = queries[j][2]
    
    Li[a] = Li[a]+c

    if b<len(Li):
        Li[b] = Li[b]-c
    
res = x = 0
for i in Li:
    x=x+i
    if(res<x):
        res=x    
        
print(res)
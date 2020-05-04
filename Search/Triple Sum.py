A = list(map(int, input().split()))

P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

P = list(sorted(set(P)))
Q = list(sorted(set(Q)))
R = list(sorted(set(R))) # To get unique sorted value
i = 0
j = 0
k = 0
res = 0

a = len(P)
b = len(Q)
c = len(R)

while j < b:
    while i < a and P[i] <= Q[j]:
        i = i+1
    
    while k < c and R[k] <= Q[j]:
        k = k+1
    
    res = res + i*k
    j = j+1

print(res)
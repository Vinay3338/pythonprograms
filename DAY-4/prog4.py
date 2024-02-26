#program to print sum of max and min in tuple matrix
t=[]
t2=[]
r,c=int(input()),int(input())
for i in range(r):
    t.append(tuple(map(int,input().split())))
for i in t:
    for j in i:
        t2.append(j)
print(t)
print(min(t2)+max(t2))
    

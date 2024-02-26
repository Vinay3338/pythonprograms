l=[]
l2=[]
r,c=int(input()),int(input())
for i in range(r):
    l.append(tuple(map(int,input().split())))
print(l)
for i in l:
    print(i)
    for j in i:
        l2.append(j)
        
print(l2)
print(sum(l2)/len(l2))

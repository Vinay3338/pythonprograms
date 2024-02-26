l=[]
r,c=map(int,input().split())
for i in range(r):
    l.append(list(map(int,input().split())))
prod=1
l1=[]
product=1
for i in l:
    print(i)
    for j in i:
        print(j)
        l1.append(j)
        product*=j
for i in l1:
    prod*=i
    #summ+=sum(i)
print(prod)
#print(l)
print(product)

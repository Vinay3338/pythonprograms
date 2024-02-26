#program to print sum of the given matrix
l=[]
r,c=map(int,input().split())
for i in range(r):
    l.append(list(map(int,input().split())))
summ=0
for i in l:
    print(i)
    summ+=sum(i)
print(summ)
#print(l)
    

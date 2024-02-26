#program to print sum of the of elements in last column of a matrix
l=[]
r,c=int(input()),int(input())
for i in range(r):
    l.append(tuple(map(int,input().split())))
l2=[]
#sum=0
for  i in l:
    #sum+=i[c-1]
    l2.append(i[c-1])
print(sum(l2))
#print(sum)

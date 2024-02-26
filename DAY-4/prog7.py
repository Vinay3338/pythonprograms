#program to make addition of 2 matrix
r,c=int(input()),int(input())
l1=[]
l2=[]
l3=[]
#l3=[0]*r
'''for i in range(r):
    l3[i]=[0]*c'''
for i in range(r):
    l1.append(list(map(int,input().split())))
for i in range(r):
    l2.append(list(map(int,input().split())))
print(l1)
print(l2)
for i in range(r):
    l4=[]
    for j in range(c):
        #l3[i][j]=l2[i][j]+l1[i][j]
        l4.append(l1[i][j]+l2[i][j])
    l3.append(tuple(l4))
#print(l3)
print(l3)

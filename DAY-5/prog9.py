#program to print average of each student in nested dict
#program to maintain students marks database
d={}
d1={}
n,m=map(int,input().split())
for i in range(n):
    k=input("enter roll no:")
    v={}
    for i in range(m):
        sub=input("enter sub name:")
        marks=int(input("enter marks:"))
        
        v[sub]=marks
    d[k]=v
print(d)
for i in d:
    print(i,"=",d[i])
for i in d:
    l=list(d[i].values())
    print("Average:",sum(l)/m)

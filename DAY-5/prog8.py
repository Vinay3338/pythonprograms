#program to maintain students marks database
d={}
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

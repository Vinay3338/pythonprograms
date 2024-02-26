#program to remove duplicates in a list
l=list(map(str,input().split()))
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)

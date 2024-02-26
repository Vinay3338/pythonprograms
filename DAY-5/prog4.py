'''n=int(input())
d={}
for i in range(2):
    keys,values=map(str,input().split())
    d[keys]=values
print(d)
#s=input()
l=list(d.vaules())
if len(l[0])==len(l[1]):
    if sorted(list(l[0]))==sorted(list(l[1])):
        print("True")
    else:
        print("False")
else:
    print("False")'''
"""
s1,s2=map(str,input().split())
if len(s1)==len(s2):
    if sorted(list(s1))==sorted(list(s2)):
        print(sorted(list(s1)))
        print(sorted(list(s2)))
        print("True")
    else:
        print("False")
else:
    print("False")
"""
s1,s2=map(str,input().split())
if len(s1)==len(s2)and sorted(list(s1))==sorted(list(s2)): 
        print(sorted(list(s1)))
        print(sorted(list(s2)))
        print("True")
else:
    print("False")

#program to print the sum of odd composite numbers in a given range
#l=list(map(int,input(),split()))
'''l1=[]
l2=[]
n,m=int(input()),int(input())
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
    if count>2:
        l1.append(i)
for i in l1:
    if i%2!=0:
        l2.append(i)
print(sum(l2))'''
def composite(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count>2:
        return 1
    else:
        return 0
n,m=int(input()),int(input())
l=[]
for i in range(n,m+1):
    if i%2!=0:
        flag=composite(i)
        if flag==1:
            l.append(i)
print(sum(l))
print(l)

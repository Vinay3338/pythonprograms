#program to print sum of odd numbers in a range
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i%2!=0:
        l1.append(i)
print(sum(l1))
'''sum=0
for i in l1:
    sum=sum+i
print(sum)'''
'''n,m=int(input()),int(input())
l2=[i for i in range(n,m+1) if i%2==0]
print(sum(l2))'''

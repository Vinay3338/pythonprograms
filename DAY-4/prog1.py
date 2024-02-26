#program to print the sum of even palindromes in a range and also print list of palindromes
l=[]
l2=[]
n,m=int(input()),int(input())
'''rev=0
while n>0:
    for i in range(n,m+1):
        digit=n%10
        rev=rev*10+digit
        n//=10
    if n==rev:
        l.append(rev)
for i in l:
    if i%2==0:
        l2.append(i)
print(l)
print(sum(l2))'''



def palindrome(n):
    sum=0
'''while n>0:
        digit=n%10
        sum=sum*10+digit
        n//=10'''
    s=str(n)
    if s==s[::-1]:
        return 1
    else:
        return 0
for i in range(n,m+1):
    flag=palindrome(i)
    if flag==1:
        l.append(i)
    if i%2==0:
        if flag==1:
            l2.append(i)
print(l)
print(l2)
print(sum(l2))


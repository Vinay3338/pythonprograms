#to print the factorial of given number
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
def strong(x):
    s=str(x)
    sum=0
    for i in s:
        sum+=fact(int(i))
    if sum==x:
        #return x
        print(x)
    '''else:
        return "not strong number"'''
'''x=int(input())
print(strong(x))'''
a,b=int(input()),int(input())
for i in range(a,b+1):
    strong(i)

#program to check armstrong or not
n=int(input("enter the number"))
sum=0
order=len(str(n))
n1=n
while n>0:
    digit=n%10
    n//=10
    sum+=digit**order
if sum==n1:
    print("it is armstrong")
else:
    print("it is not armstrong")
    

#program to check its is prime or not.
n=int(input("enter number"))
f=0
for i in range(1,n+1):
    if n%i==0:
        print(i)
        f+=1
print(f)
if f==2:
    print("the number is prime")
elif n==1 or n==0:
    print("not define")
else:
    print("the number is not a prime")

'''for i in range(2,(n//2)+1): #half iterations
    if n%i==0:
        print("the number is prime")
        break
else:
    print("the number is not a prime")'''
    

#program to check the number perfect number or not
n=int(input("enter the number"))
f=0
for i in range(1,n):
    if n%i==0:
        f+=i
if f==n:
    print("perfect number")
else:
    print("not perfect number")
print(f)
    

    

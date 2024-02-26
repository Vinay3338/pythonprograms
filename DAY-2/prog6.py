#program to print reverse of number
n=int(input("enter the number"))
rev=0
'''while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)'''
for i in range(n):
    if n>0:
        digit=n%10
        rev=rev*10+digit
        n//=10
    else:
        break
print(rev)

    

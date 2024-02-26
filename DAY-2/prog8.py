#program to print prime numbers in range using range
def prime(n,m):
    
    for i in range(n,m+1):
        fact=0
        x=i
        for j in range(1,m+1):
            if x%j==0:
                fact+=1
        if fact==2:
            print(i)
n,m=int(input()),int(input())
prime(n,m)

        

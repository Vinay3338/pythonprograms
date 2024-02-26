'''n=int(input())
d={}
count=0
for i in range(1,n):
    
    if n%i==0:
        count+=1
        if count<=2:
            k="prime"
        else:
            k="composite"
    d[i]=k
print(d)'''

def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return "composite"
        else:
            return "prime"
n=int(input())
d={}
for i in range(n):
    k=i+1
    v=isprime(k)
    d[k]=v
print(d)

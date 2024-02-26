#ip's and it's name
n,m=map(int,input().split())
d={}
#d2={}
for i in range(n):
    keys,values=map(str,input().split())
    d[keys]=values
print(d)
for i in range(m):
    skeys,svalues=map(str,input().split())
    #d2[skeys]=svalues
    for i in d:
        if d[i]==svalues[:-1]:
        #if skeys in d.keys() and svalues[::-1] in d.values():
            print(f"{skeys} {svalues}#{i}")
            print("{},{},#{}".format(skeys,svalues,i))
        
        
    

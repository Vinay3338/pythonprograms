#phone numbers
d={}
n=int(input())
for i in range(n):
    keys,values=map(str,input().split())
    d[keys]=values
print(d)

for i in d:
    m=input()
    if m==i:
        print(d[i])
    else:
        print("Not found")

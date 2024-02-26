
x,y=map(int,input().split())
p=4
if x<=y:
    np=0
else:
    xc=x-y
    if xc%4==0:
        np=xc//4
    else:
        np=(xc//4)+1
print(np)

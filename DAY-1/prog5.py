x,y=map(float,input().split(" "))
print(x,y)
'''if x<y:
    if x%5==0:
        print(y-x)
    else :
        print(y)
else :
    print(y)'''
if x<=y and x%5==0:
    print(y-x)
else:
    print(y)
    


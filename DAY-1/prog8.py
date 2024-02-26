a,b,c,d=map(float,input().split())
a=a-a*c//100
b=b-b*d//100
if a<b:
    print("first")
elif a>b:
    print("second")
else:
    print("any")

import math
print("pizzas and slices")
n,x=map(int,input().split())
ns=n*x
'''if ns%4==0:
    print(ns//4)
else:
    print(ns//4+1)'''
np=math.ceil(ns/4)
print(np)

n=input("enter no of digits:")
d=input("enter insert number:")
num=input("enter number:")
for i in range(len(num)):
    if d<num[i]:
        print(num[:i]+d+num[i:])
    elif d==num[i]:
        print(num[:i]+d+num[i:])
        
else:
    print(num+d)
'''for i in range(len(n)):
    if int(n[i]) < int(d):
        print(num[:i]+d+num[i:])
        break
    elif int(n[i])==int(d):
        print(num[:i]+d+num[i:])
        break
else:
    print(num+d)'''
        
        
    

                  
               
               


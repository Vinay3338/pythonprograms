n,d=map(int,input().split())
l=list(map(int,input().split()))
flag=0
'''for i in range(len(l)):
    for j in range(i):
        if (l[j]-l[i])==d:
            print("True")
            break
        else:
          print("False")'''
for i in l:
    for j in l:
        if i-j==d:
            flag=1
'''if flag==0:
    print(False)
else:
    print("True")'''
print(True if flag==1 else False)

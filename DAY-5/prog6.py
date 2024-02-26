#print the first repeating char
s=input()
count=0
'''for i in s:
    if s.count(i)>1:
        print(i)
        break
else:
    print('.')'''
for i in s:
    if i in s:
        count+=1
    if count>1:
        print(i)
        break
else:
    print('.')

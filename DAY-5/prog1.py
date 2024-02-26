#program to take dict as i/p & print keys&values of a dict
n=int(input())
d={}
for i in range(n):
    name=input("key:")
    vaules=input("value:")
    d[name]=vaules
print(d)
print(d.keys())
print(d.values())
for i in d:
    print("key:",i,"vaules:",d[i])
    print(f"key:{i} value:{d[i]}")
    print("key:{} value:{}".format(i,d[i]))
for i in d.keys():
    print(i)
for i in d.values():
    print(i)

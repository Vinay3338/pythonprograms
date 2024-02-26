#program to make encryption & decryption using keyvalue using functions
def encryption(s,k):
    encval=""
    for i in range(len(s)):
        temp=ord(s[i])+k
        encval+=chr(temp)
        print(temp)
        print(chr(temp))
    print(encval)
def decryption(s,k):
    decval=""
    for i in range(len(s)):
        temp=ord(s[i])-k
        decval+=chr(temp)
        print(chr(temp))
    print(decval)
k=int(input("enter keyvalue:"))        
s=input("enter string:")
op=input("select operation:")    
if op=="encrypt":
    encryption(s,k)
elif op=="decrypt":
    decryption(s,k)
else:
    print("invalid operation")
    

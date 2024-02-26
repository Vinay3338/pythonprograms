#program to check panagram or not
import string
s=input()
s=s.lower() 
#s1={'a','b','c','d','e','f','g','h','i','j','k','l',''}
s1=string.ascii_lowercase
if set(s)==set(s1):
    print("panagram")
else:
    print("not panagram")

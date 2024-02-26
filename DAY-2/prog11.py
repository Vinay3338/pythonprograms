#write a program to remove dupicates
string1=input()
string2=""
for i in string1:
    if i not in string2:
        string2+=i
print(string2)
        
    

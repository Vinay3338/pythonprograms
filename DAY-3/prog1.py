#program to print the smallest vowel which is repeating odd number of times in a string
s=input()
s1=""
oc=0
for i in range(len(s)):
    if i%2!=0:
        if s[i] in "aeiouAEIOU":
            oc+=1
            s1+=s[i]
            print(s[i])
print(oc)
print(min(s1))

'''for i in s:
    if i in "aeiouAEIOU":
        if s.count(i)%2!=0:
            s1+=i
print(min(s1))'''
        
            

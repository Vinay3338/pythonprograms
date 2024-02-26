#program to print count of vowels in both even and odd positions
s=input()
for i in range(len(s)):
    ecount=0
    ocount=0
    if i%2==0:
        if s[i] in "aeiouAEIOU":
            ecount+=1
    else:
        if s[i] in "aeiouAEIOU":
            ocount+=1
        
print(ecount,ocount)
            

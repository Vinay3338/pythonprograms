#program to print count of vowels & list of vowels in the each word and list of word in sentence using functions
#s=input()
def vowels_word(n):
    print(n)
    count=0
    s1=[]
    for i in n:
        if i in 'aeiouAEIOU':
            count+=1
            s1.append(i)
            print(i)
    print(count)
    print(tuple(s1))
l=input().split()
for i in l:
    #counting(i)
    vowels_word(i)

'''def counting(s):
    print(s)
    s1,vc='',0
    for i in s:
        if i in "aeiouAEIOU":
            vc+=1
            s1+=i
    print("vowel count:",vc)
    print(list(set(s1)))
l=input().split()
for i in l:
    counting(i)'''

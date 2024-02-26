#program to print an armstrong number using strings and functions
def armstrong(n,m):
    for i in range(n,m+1):
        sum=0
        s=str(i)
        for j in s:
            sum+=int(j)**len(s)
        if str(sum)==i:
            print(i)
n,m=int(input()),int(input())
armstrong(n,m)           
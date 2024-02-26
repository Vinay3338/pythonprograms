#sum of n natural numbers using recursion
def sumofn(n):
    sum=1
    if n<1:
        return 0
    else:
        return n+sumofn(n-1)
n=int(input())
sum=sumofn(n)
print(sum)

#program to print n natural numbers
def naturalnumbers(n):
    sum=0
    if n<1:
        return 1
    else:
        naturalnumbers(n-1)
        print(n)
n=int(input())
naturalnumbers(n)

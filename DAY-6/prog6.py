class a:
    def __init__(self,data):
        self.data=data
    def even(self,n):
        if n%2==0:
            return "even"
class b(a):
    def __init__(self,data):
        self.data=data
        super().__init__(data)
        print(self.even(self.data))
        print(self.odd(self.data))
    def odd(self,n):
        if n%2!=0:
            return "odd"
x=int(input())
obj=b(x)

#multi level inheritance
class parent:
    def func1(self,data1):
        self.data1=data1
        print("three variables:",data1)
class child(parent):
    def func2(self,data1,data2):
        self.data2=data2
        #super().func1(data1)
        print("three variables:",data1,data2)
class child1(child):
    def func3(self,data1,data2,data3):
        self.data3=data3
        #super().func2(data2)
        print("three variables:",data1,data2,data3)
obj=child1()
obj.func3(input(),input(),input())
'''
class a:
    def __init__(self,data1):
        print("data:",data1)
class b(a):
    def __init__(self,data1,data2):
        super().__init__(data1)
        print("data:",data2)
class c(b):
    def __init__(self,data1,data2,data3):
        self.data1=data1
        self.data2=data2
        super().__init__(data1,data2)
        self.data3=data3
        print("data:",data3)
A,B,C=map(str,input().split())
obj=c(A,B,C)'''





    

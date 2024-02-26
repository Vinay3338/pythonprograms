class ece:
    def sec1(self,name,sec):
        self.name=name
        self.sec=sec
        print(name,sec)
    def sec2(self,name,sec,age):
        self.name=name
        self.sec=sec
        self.age=age
        print(name,sec,age)
    def __init__(self,name,sec,age):
        self.name=name
        self.age=age
        print(name,age)
obj=ece("nish",2,"20")
#obj1=ece("nish","20")
obj.sec1("nish","2")
obj.sec2("nish","2",20)


class a:
    def hi(self):
        print("parent")
class b(a):
    def hi(self,hello):
        print("chid1")
class c(a):
    def __init__(self):
        print("child2")
d=b()
d.hi()
e=c()
e.hi()

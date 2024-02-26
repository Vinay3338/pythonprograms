class strm1:
    def __init__(self,data):
        self.data=data
    def strlen(self,data):
        print("Length:",len(self.data))
class strm2:
    def __init__(self,data):
        self.data=data
    def strlower(self,data):
        print(self.data.lower())
class strm3:
    def __init__(self,data):
        self.data=data
    def strupper(self,data):
        print(self.data.upper())
class prog(strm1,strm2,strm3):
    def __init__(self,data):
        self.data=data
        self.strlower(data)
        self.strupper(data)
        self.strlen(data)
        print("completed")
obj=prog(input())
    

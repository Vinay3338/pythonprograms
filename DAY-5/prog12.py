class training:
    def __init__(self,lang):
        self.lang=lang
    def sec1(self):
        print("training sec1:",self.lang)
    def sec2(self):
        print("training sec2:",self.lang)
obj=training("python")
obj.sec1()
obj.sec2()

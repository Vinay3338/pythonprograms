#single inheritance using 5 sub classes
class training:
    def __init__(self):
        print("intro")
class ece1(training):
    def __init__(self):
        super().__init__()
        print("section1")
class ece2(ece1):
    def __init__(self):
        super().__init__()
        print("section2")
class ece3(ece2):
    def __init__(self):
        super().__init__()
        print("section3")
class ece4(ece3):
    def __init__(self):
        super().__init__()
        print("section4")
class ece5(ece4):
    def __init__(self):
        super().__init__()
        print("section5")

#obj0=ece1()
obj=ece5()

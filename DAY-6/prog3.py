#program to print factorial of given number using class,methods&recursion
class rec:
    def __init__(self,data):
        self.data=data
        print(self.log(data))
        #print(self.find_fact())
    '''def find_fact(self):
        return self.log(self.data)'''
    def log(self,num):
        fact=1
        if num>1:
            return num*self.log(num-1)
        else:
            return 1
obj=rec(int(input()))
            

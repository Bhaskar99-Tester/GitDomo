from opp import Calculator

class Child(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self,8,5)

    def Getcompletedata(self):
        return self.num2+self.num+self.sum()

C = Child()

print(C.Getcompletedata())
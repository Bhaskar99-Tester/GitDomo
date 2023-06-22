class Calculator:
    num = 100

    def __init__(self,a,b):
        self.firstnum = a
        self.secondnum = b
        print('object is created')

    def getData(self):
        print("i am now executing as method in class")

    def sum(self):
        return self.firstnum + self.secondnum

obj = Calculator(5, 6)

obj.getData()
result = obj.sum()
print(result)
print(obj.num)

obj2 = Calculator(9,6)
print(obj2.sum())

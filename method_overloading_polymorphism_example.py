class Sum:
    def sum(self,a,b):
        print(a + b)

class SumThree:
    def sum(self,a,b,c):
        print(a + b + c)

class SumFour:
    def sum(self,a,b,c,d):
        print(a + b + c + d)

obj1 = Sum()
obj2 = SumThree()
obj3 = SumFour()

obj1.sum(5,2)
obj2.sum(5,6,8)
obj3.sum(5,4,3,1)
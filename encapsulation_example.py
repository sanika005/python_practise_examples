class Base:
    def __init__(self):
        self.a = 'public_member_of_base'
        self.__c = 'private_member'

class Derived(Base):
    def __init__(self):
        self.b = 'public_member_of_derived'
        Base.__init__(self)
        self.a1 = self.a
        # It will give AttributeError
        # self.c1 = self.__c

    def print(self):
        print(f"The value of b: {self.b}")
        print(f"The value of a1: {self.a1}")
        # print(f"The value of c1: {self.c1}")

obj = Derived()
obj.print()
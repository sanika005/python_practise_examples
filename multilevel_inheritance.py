# Base class
class Grandfather:
    def __init__(self,grandfathername) -> None:
        self.grandfathername = grandfathername

# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername) -> None:
        self.fathername = fathername
        Grandfather.__init__(self,grandfathername)

# Derived class
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self,fathername,grandfathername)

    def print_names(self):
        print(f"Grandfather's name: {self.grandfathername}")
        print(f"Father's name: {self.fathername}")
        print(f"Son's name: {self.sonname}")

obj = Son("Tommy","Rodger","Newton")
obj.print_names()
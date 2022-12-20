# Base class
class Mother:
    mother_name = ""

    def mother(self):
        print(self.mother_name)

# Base class
class Father:
    father_name = ""

    def father(self):
        print(self.father_name)

# Derived class
class Children(Mother,Father):
    def children(self):
        print(f"The mothername is:{self.mother_name}")
        print(f"The fathername is:{self.father_name}")

obj = Children()
obj.mother_name = "Trisha"
obj.father_name = "Shan"
obj.children()
class Parent:
    def parent(self):
        print("This function is in the parent class")

class Child1(Parent):
    def child1(self):
        print("This function is in child 1")

class Child2(Parent):
    def child2(self):
        print("This function is in child 2")

ch1 = Child1()
ch2 = Child2()
ch1.child1()
ch1.parent()
ch2.child2()
ch2.parent()
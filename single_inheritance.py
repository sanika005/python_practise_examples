# Base class
class Parent:
    def func1(self):
        print("This function is in the Parent class")

# Derived class
class Child(Parent):
    def func2(self):
        print("This function is in the Child class")

child = Child()
child.func1()
child.func2()
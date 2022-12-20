class Dog:
    attr1 = "mammal"

    def __init__(self, name) -> None:
        self.name = name

    
rodger = Dog("rodger")
tommy = Dog("tommy")

print("rodger is a {}".format(rodger.attr1))
print("tommy is a {}".format(tommy.attr1))

print("My name is: {}".format(rodger.name))
print("My name is: {}".format(tommy.name))
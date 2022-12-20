# What are class and instance attributes?
# What are class and instance methods?
# Formula for Volume of cylinder is: V = pi*r**2*h
from math import pi
class Cylinder:
    # class attr
    pi_value = pi
    
    def __init__(self,radius,height):
        # instance attr
        self.radius = radius
        self.height = height

    # instance method
    def volume(self):
        volume = (Cylinder.pi_value)*(self.radius**2)*(self.height)
        return volume

    # class method
    @classmethod
    def description(cls):
        return f"***This is Cylinder class that computes the volume of the cylinder***"

obj1 = Cylinder(20,30)
obj2 = Cylinder(2,15)
obj3 = Cylinder(4,3)

print("PI value for obj1: {} and obj2: {}".format(obj1.pi_value,obj2.pi_value)) # Call class attr with object
print("height value for obj1: {} and obj2: {}".format(obj1.height,obj2.height)) # Call instance attr with object
print("radius value for obj1: {} and obj2: {}".format(obj1.radius,obj2.radius)) # Call instance attr with object
print("PI value for both obj1 and obj2 is {}".format(Cylinder.pi_value))    # Call class attribute with Class directly

# Call instance method
print('The volume of cylinder is: {}'.format(obj3.volume()))
# Call classmethod via class
print('The description is: {}'.format(Cylinder.description()))
# Call classmethod via instance
print('The description is: {}'.format(obj3.description()))
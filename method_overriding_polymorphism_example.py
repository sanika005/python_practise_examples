class Bird:
    def intro(self):
        print("There are many types of birds")

    def flight(self):
        print("Some birds can fly but some birds cannot fly")

class Sparrow(Bird):
    def flight(self):
        print("The bird sparrow can fly")

class Ostrich(Bird):
    def flight(self):
        print("The bird ostrich can't fly")

obj_bird = Bird()
obj_spr = Sparrow()
obj_ostr = Ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.flight()

obj_ostr.flight()
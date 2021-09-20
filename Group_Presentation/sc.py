# polymorphism with inheritance

class Bird:
    def intro(self):
        print("There are many types of birds")

    def flight(self):
        print("Most birds can fly but some cannot \n")


class Eagle(Bird) :
    def flight(self):
        print("Eagles can fly \n")


class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly")


object_bird = Bird()
object_eagle = Eagle()
object_ostrich = Ostrich()

object_bird.intro()
object_bird.flight()

object_eagle.intro()
object_eagle.flight()

object_ostrich.intro()
object_ostrich.flight()



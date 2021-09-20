# built-in polymorphic functions

print(len("example"))   # here the built-in length function is being used for a string

print(len([1, 2, 3]))   # here the built-in length function is being used for a list


# user-defined polymorphic functions

def addition(*multi_values):        # creating a function for adding multiple numbers
    answer = sum(multi_values)      # storing the result of the built-in sum function into a variable called answer
    return answer                   # sending the value back to the main program


print(addition(1, 2, 3))    # using the addition function on three values

print(addition(4, 5))       # using the addition function on two values


# polymorphism with class methods

class England:
    def capital(self):
        print("London is the capital of England")

    def language(self):
        print("English is the primary language")

    def population_2018(self):
        print("In 2018, the population was 55.98 million \n")


class Madagascar:
    def capital(self):
        print("Antananarivo is the capital of Madagascar")

    def language(self):
        print("Malagasy is the primary language")

    def population_2018(self):
        print("In 2018, the population was 26.26 million")


object_england = England()
object_madagascar = Madagascar()

for country in (object_england, object_madagascar):
    country.capital()
    country.language()
    country.population_2018()


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


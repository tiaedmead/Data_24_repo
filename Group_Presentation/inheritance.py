# single inheritance - when a child class inherits only a single parent class

# class Parent:
#     def first(self):
#         print("first function")
#
# class Child(Parent):
#     def second(self):
#         print("second function")
#
#
# object = Child()
# object.first()      # using the child class, you can access the parent class
# object.second()

# multiple inheritance - when a child class inherits from more than one parent class

# class Parent:
#     def first(self):
#         print("first function")
#
#
# class Parent2:
#     def second(self):
#         print("second function")
#
#
# class Child(Parent, Parent2):
#     def third(self):
#         print("third function")
#
#
# obj = Child()
# obj.first()      # using the child class, you can access the parent class
# obj.second()
# obj.third()

# multilevel inheritance - when a child class becomes a parent class for another child

# class Parent:
#     def first(self):
#         print("first function")
#
#
# class Child(Parent):
#     def second(self):
#         print("second function")
#
#
# class Child2(Child):
#     def third(self):
#         print("third function")
#
#
# obj = Child2()
# obj.first()
# obj.second()
# obj.third()

# hierarchical inheritance - multiple inheritance from the same parent class

# class Parent:
#     def first(self):
#         print("first function")
#
# 
# class Child(Parent):
#     def second(self):
#         print("second function")
#
#
# class Child2(Parent):
#     def third(self):
#         print("third function")
#
#
# obj = Child()
# obj2 = Child2()
# obj.first()
# obj.second()
# obj2.third()        # only obj2 can call the third function
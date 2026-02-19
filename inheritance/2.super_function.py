# Using super() in __init__

class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal constructor called")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # call parent constructor
        self.breed = breed

d = Dog("Buddy", "Labrador")
print(d.name)
print(d.breed)

""""""""""""""""""""""""""

# Using super() to extend a method

class Person:
    def greet(self):
        print("Hello!")

class Student(Person):
    def greet(self):
        super().greet()  # call parent method
        print("I am a student")

s = Student()
s.greet()

""""""""""""""""""""""""""

# super() with calculations

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  # pass same value twice

sq = Square(5)
print(sq.width)
print(sq.height)

""""""""""""""""""""""""""

# super() in multiple inheritance

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        super().show()
        print("Class B")

class C(B):
    def show(self):
        super().show()
        print("Class C")

c = C()
c.show()

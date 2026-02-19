# Basic overriding

class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):  # Override
        print("Woof")

d = Dog()
d.speak()  # Woof

""""""""""""""""""""""""""

# Overriding with different behavior

class Shape:
    def area(self):
        print("Area is undefined")

class Circle(Shape):
    def area(self):
        print("Area = pi * r^2")

c = Circle()
c.area()  

""""""""""""""""""""""""""

# Overriding and using super()

class Person:
    def greet(self):
        print("Hello")

class Student(Person):
    def greet(self):  # Override but extend
        super().greet()
        print("I am a student")

s = Student()
s.greet()
# Hello
# I am a student

""""""""""""""""""""""""""

# Overriding in multi-level inheritance

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):  # Override
        print("Car is driving")

class ElectricCar(Car):
    def move(self):  # Override again
        print("Electric car is silently driving")

e = ElectricCar()
e.move()  # Electric car is silently driving

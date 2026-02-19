
class Car:
    wheels = 4

car1 = Car()
print("Car wheels:", car1.wheels)

""""""""""""""""""""""""""

class Dog:
    legs = 4

dog1 = Dog()
dog2 = Dog()
dog3 = Dog()

print("Dog1 legs:", dog1.legs)
print("Dog2 legs:", dog2.legs)
print("Dog3 legs:", dog3.legs)

""""""""""""""""""""""""""

class Person:
    age = 18

p1 = Person()
p2 = Person()

p1.age = 25 

print("P1 age:", p1.age)
print("P2 age:", p2.age)

""""""""""""""""""""""""""

class Book:
    pages = 100

b1 = Book()
print("Book pages:", b1.pages)

del b1 




# Modifying and deleting object properties

class Car:
    def __init__(self, brand):
        self.brand = brand

car1 = Car("Toyota")

car1.brand = "BMW"  # Modify property
print(car1.brand)  # BMW

""""""""""""""""""""""""""

class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")

del p1.name  # Delete property
# print(p1.name)  # Error

""""""""""""""""""""""""""

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

b1 = Book("Python Basics", 200)

b1.title = "Advanced Python"
b1.pages = 350

print(b1.title)  
print(b1.pages)

""""""""""""""""""""""""""

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

l1 = Laptop("Dell", 1200)

del l1.price  # Delete only price
print(l1.brand)  


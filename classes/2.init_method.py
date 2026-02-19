# The __init__() Method

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s1 = Student("Anna", 10)
print(s1.name)
print(s1.grade)

""""""""""""""""""""""""""

class User:
    def __init__(self, username, role="user"):
        self.username = username
        self.role = role

u1 = User("alex")
u2 = User("admin01", "admin")

print(u1.username, u1.role)
print(u2.username, u2.role)

""""""""""""""""""""""""""

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car("Toyota", "Corolla", 2022)
print(car1.brand)
print(car1.model)
print(car1.year)

""""""""""""""""""""""""""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height  # считаем площадь сразу

r1 = Rectangle(5, 3)
print("Width:", r1.width)
print("Height:", r1.height)
print("Area:", r1.area)








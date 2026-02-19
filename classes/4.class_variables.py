# Class variables vs instance variables

class Cat:
    species = "Felis"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

cat1 = Cat("Milo")
cat2 = Cat("Luna")

print(cat1.species)
print(cat2.species)  

cat1.name = "Oliver"
print(cat1.name) 
print(cat2.name) 

""""""""""""""""""""""""""

class Car:
    wheels = 4  # Class variable

    def __init__(self, brand):
        self.brand = brand  # Instance variable

car1 = Car("Toyota")
car2 = Car("Honda")

print(car1.wheels)  
print(car2.wheels) 

car2.brand = "BMW"
print(car1.brand) 
print(car2.brand)  

""""""""""""""""""""""""""

class Student:
    school = "Greenwood"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

s1 = Student("Alice")
s2 = Student("Bob")

print(s1.school) 
print(s2.school) 

s1.name = "Anna"
print(s1.name)
print(s2.name)

""""""""""""""""""""""""""

class Phone:
    brand = "Samsung"  # Class variable

    def __init__(self, model):
        self.model = model  # Instance variable

p1 = Phone("Galaxy S23")
p2 = Phone("Galaxy A54")

print(p1.brand)  
print(p2.brand)  

p2.model = "Galaxy S24"
print(p1.model) 
print(p2.model) 

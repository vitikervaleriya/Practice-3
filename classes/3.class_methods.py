# Class Methods
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is " + self.name)

a1 = Animal("Buddy")
a1.speak()

""""""""""""""""""""""""""

# Methods with Parameters
class MathOperations:
    def subtract(self, a, b):
        return a - b

math = MathOperations()
print(math.subtract(10, 4))

""""""""""""""""""""""""""

# Methods Accessing Properties
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def description(self):
        return f"{self.title} has {self.pages} pages"

b1 = Book("Python Basics", 250)
print(b1.description())

""""""""""""""""""""""""""

# Methods Modifying Properties 
class Counter:
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1
        print("Count is now:", self.count)

c1 = Counter()
c1.increase()
c1.increase()

""""""""""""""""""""""""""

# The __str__() Method
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __str__(self):
        return f"{self.name} - population {self.population}"

city1 = City("Oslo", 700000)
print(city1)

""""""""""""""""""""""""""

# Delete Methods
class Greeting:
    def say_hi(self):
        print("Hi!")

g1 = Greeting()
del Greeting.say_hi

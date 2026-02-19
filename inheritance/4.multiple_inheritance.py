# Basic multiple inheritance
class Flyer:
    def fly(self):
        print("Flying")

class Swimmer:
    def swim(self):
        print("Swimming")

class Duck(Flyer, Swimmer):
    pass

d = Duck()
d.fly()   # Flying
d.swim()  # Swimming

""""""""""""""""""""""""""

# Multiple inheritance with unique method
class Writer:
    def write(self):
        print("Writing a story")

class Painter:
    def paint(self):
        print("Painting a picture")

class Artist(Writer, Painter):
    pass

a = Artist()
a.write()  # Writing a story
a.paint()  # Painting a picture

""""""""""""""""""""""""""

# Multiple inheritance with __init__
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Wheels:
    def __init__(self, count):
        self.count = count

class Car(Engine, Wheels):
    def __init__(self, horsepower, count):
        Engine.__init__(self, horsepower)
        Wheels.__init__(self, count)

c = Car(200, 4)
print(c.horsepower)  # 200
print(c.count)       # 4

""""""""""""""""""""""""""

# Multiple inheritance with method overriding
class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    def greet(self):
        super().greet()  # calls A's greet because of MRO
        print("Hello from C")

c = C()
c.greet()
# Hello from A
# Hello from C

# Parent Class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print_name(self):
        print(self.firstname, self.lastname)


# Child Class - Student
class Student(Person):
    def study(self):
        print(self.firstname, "is studying")


# Child Class - Teacher
class Teacher(Person):
    def teach(self):
        print(self.firstname, "is teaching")


# Child Class - Worker
class Worker(Person):
    def work(self):
        print(self.firstname, "is working")


# Child Class - Athlete
class Athlete(Person):
    def train(self):
        print(self.firstname, "is training")


# Creating objects
s = Student("Mike", "Olsen")
t = Teacher("Anna", "Smith")
w = Worker("John", "Brown")
a = Athlete("Leo", "King")

# Using inherited method
s.print_name()
t.print_name()
w.print_name()
a.print_name()

# Using child-specific methods
s.study()
t.teach()
w.work()
a.train()

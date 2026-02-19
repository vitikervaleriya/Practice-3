#Positional
#Default



# Parameters and Arguments
def greet(name, age):
    print("Hello", name + "!")
    print("You are", age, "years old.")

greet("Anna", 18)

""""""""""""""""""""""""""

def rectangle_area(length, width):
    print("Area =", length * width)

rectangle_area(5, 3)

""""""""""""""""""""""""""

def repeat_word(word, times):
    print(word * times)

repeat_word("Hi ", 3)

""""""""""""""""""""""""""

def difference(a, b):
    print("Difference =", a - b)

difference(10, 4)


# Default Parameter Values

def greet(name="friend"):
    print("Hello", name)

greet()
greet("Linus")

""""""""""""""""""""""""""

def my_country(country="Norway"):
    print("I am from", country)

my_country("Sweden")
my_country()
my_country("Brazil")

""""""""""""""""""""""""""

def show_age(name="friend", age=18):
    print(name, "is", age, "years old")

show_age("Anna", 20)
show_age("John")
show_age()

""""""""""""""""""""""""""

def favorite_animal(name="friend", animal="dog"):
    print(name, "likes", animal)

favorite_animal("Emily", "cat")
favorite_animal("Lucas")
favorite_animal()


# Keyword Arguments

def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function(animal="dog", name="Buddy")
my_function(name="Whiskers", animal="cat")

""""""""""""""""""""""""""

def favorite_food(food, person):
    print(person, "loves", food)

favorite_food(food="pizza", person="Anna")
favorite_food(person="John", food="sushi")

""""""""""""""""""""""""""

def car_info(make, model):
    print("Car make:", make)
    print("Car model:", model)

car_info(make="Toyota", model="Corolla")
car_info(model="Mustang", make="Ford")

""""""""""""""""""""""""""

def travel(destination, days):
    print("I will travel to", destination)
    print("It will take", days, "days")

travel(destination="Paris", days=5)
travel(days=10, destination="Tokyo")



def animal_name(animal, name):
   print("Name of the", animal, "is", name)

animal_name(name = "Lili", animal = "cat")
animal_name(animal = "dog", name = "Gyf")







# Positional Arguments

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

# Mixing Positional and Keyword Arguments

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)


#Passing Different Data Types

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)



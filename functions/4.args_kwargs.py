"""# Arbitrary Arguments - *args

def sum_numbers(*nums):
    total = 0
    for n in nums:
        total += n
    return total

print(sum_numbers(4, 5, 6))
print(sum_numbers(10, 20))

""""""""""""""""""""""""""

def join_words(*words):
    return " ".join(words)

print(join_words("Python", "is", "fun"))
print(join_words("Hello", "world"))

""""""""""""""""""""""""""

def multiply_numbers(*nums):
    result = 1
    for n in nums:
        result *= n
    return result

print(multiply_numbers(2, 3, 4))
print(multiply_numbers(5, 6))

""""""""""""""""""""""""""

def greet_all(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet_all("Hello", "Anna", "John", "Lucas")
greet_all("Hi", "Emily")






# Arbitrary Keyword Arguments - **kwargs

def show_person(**info):
    print("Name:", info["name"])
    print("Age:", info["age"])

show_person(name="Anna", age=22)
show_person(name="John", age=30)

""""""""""""""""""""""""""

def show_all(**data):
    print("Type:", type(data))
    print("All data:", data)

show_all(city="Paris", country="France", language="French")
show_all(job="Developer", experience=5)
"""
""""""""""""""""""""""""""

def user_profile(username, **details):
    print("Username:", username)
    print("Details:")
    for key, value in details.items():
        print(" ", key + ":", value)

user_profile("anna123", age=22, city="Berlin", hobby="reading")
user_profile("john456", age=30, country="USA", profession="engineer")

""""""""""""""""""""""""""

def calculate(**numbers):
    total = 0
    for key, value in numbers.items():
        total += value
    return total

print(calculate(a=5, b=10, c=15))
print(calculate(x=100, y=200))

            









# Combining *args and **kwargs

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")










# Unpacking Arguments
# Using * to unpack a list into arguments:
# Using ** to unpack a dictionary into keyword arguments
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)



def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")
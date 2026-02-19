# Return Values

def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)
print(get_greeting())

""""""""""""""""""""""""""

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print(result)
print(add_numbers(10, 20))

""""""""""""""""""""""""""

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))

""""""""""""""""""""""""""

def greet(name):
    return "Hello, " + name + "!"

print(greet("Anna"))
print(greet("John"))


# Returning Different Data Types


def greet_person(name):
    return "Hello, " + name + "!"

print(greet_person("Emily"))
print(greet_person("Lucas"))

""""""""""""""""""""""""""

def square_number(n):
    return n * n

print(square_number(5))
print(square_number(10))

""""""""""""""""""""""""""

def create_range(n):
    return list(range(1, n+1))

numbers = create_range(5)
print(numbers)

""""""""""""""""""""""""""

def get_book():
    return {"title": "Python Basics", "pages": 200, "author": "John"}

book = get_book()
print(book["title"])
print(book["pages"])
print(book["author"])


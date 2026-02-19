# Calling a Function

def calculator(a, b, operation):   
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "Division by zero error"
    else:
        return "Invalid operation"
    
""""""""""""""""""""""""""

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0  
    for letter in text:
        if letter in vowels:
            count += 1         
    return count
print(count_vowels("Hello World"))

""""""""""""""""""""""""""
# Using doctring
def is_leap_year(year):
    """
    Checking leap year
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap year"
    else:
        return "Not a leap year" 
print(is_leap_year(2024))

""""""""""""""""""""""""""
def analyse(num):
    if num % 2 == 0:
      return "Even"
    elif num % 2 != 0:
       return "Odd"
    else: 
       return "Zero"
print(analyse(8))

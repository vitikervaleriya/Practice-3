# Using Lambda with map()

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  

""""""""""""""""""""""""""

def double_list(numbers):
    return list(map(lambda x: x * 2, numbers))

print(double_list([1, 2, 3, 4])) 

""""""""""""""""""""""""""

words = ["hello", "world", "python"]
upper_words = list(map(lambda w: w.upper(), words))
print(upper_words) 

""""""""""""""""""""""""""

celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)  

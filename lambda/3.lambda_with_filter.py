# Using Lambda with filter()

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # [1, 3, 5, 7]

"""""""""""""""""""""""""" 

numbers = [1, 4, 6, 8, 10, 3, 7]
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)  # [6, 8, 10, 7]

"""""""""""""""""""""""""" 

words = ["apple", "dog", "banana", "cat", "grape"]
long_words = list(filter(lambda w: len(w) > 4, words))
print(long_words)  # ['apple', 'banana', 'grape']

"""""""""""""""""""""""""" 

numbers = [-5, 0, 7, -2, 10, 3]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(positive_numbers)  # [7, 10, 3]

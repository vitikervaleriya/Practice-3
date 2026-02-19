# Using Lambda with sorted()

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students) 

"""""""""""""""""""""""""" 

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  

"""""""""""""""""""""""""" 

numbers = [3, -1, -7, 4, 0]
sorted_by_abs = sorted(numbers, key=lambda x: abs(x))
print(sorted_by_abs) 

"""""""""""""""""""""""""" 

words = ["banana", "apple", "grape", "kiwi"]
sorted_by_last_letter = sorted(words, key=lambda x: x[-1])
print(sorted_by_last_letter) 

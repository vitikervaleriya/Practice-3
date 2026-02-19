# Lambda Functions

double = lambda x: x * 2
print(double(5))  
print(double(11)) 

"""""""""""""""""""""""""" 

add = lambda a, b: a + b
print(add(3, 7))   
print(add(10, 20)) 

"""""""""""""""""""""""""" 

is_even = lambda n: n % 2 == 0
print(is_even(4))  
print(is_even(7))  

"""""""""""""""""""""""""" 

def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11)) 
print(mytripler(11)) 

"""
def name_of_function():
    some_code
    return variable


name_of_function()
"""

# def function():
#     print('The function is called')

# function()

# # otvet budet The function is called

# def function():
#     print('The function is called')
#     return 'Makers'

# print(function())

# otvet budet 
# The function is called
# Makers


# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1 + num2)
#     return num1 - num2

# print(substract())

# otvet budet 
# 25
# 15

# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1 + num2)
#     return num1 - num2

# substract()

# otvet budet 25

# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1 + num2)
#     return num1 - num2

# # substract()

# variable = substract()
# print(variable)

# otvet budet 
# 25
# 15


# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1 + num2)
#     return num1 - num2


# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, substract()]
# print(list_)

# otvet budet 
# 25
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1 + num2)
#     return num1 - num2

# def function():
#     print('Im calling substract function')
#     variable = substract()
#     return variable

# print(function())

# otvet budet 
# Im calling substract function
# 25
# 15


# def multiply(a, b):
#     return a * b
# num1 = 70
# num2 = 10
# print(multiply(num1, num2))

# print(num1)
# print(num2)

# otvet budet 700


# def welcome(name, last_name):
#     return f'Welcome, {name} {last_name}'

# name = input()
# last_name = input()
# print(welcome(name, last_name))

# otvet budet
# John
# Smow
# Welcome, John Smow


# def get_word(word):
#     list_letters = list(word)
#     print(list_letters)
#     return list_letters

# def get_vowels(letters):
#     vowels = ['a', 'o', 'y', 'i', 'e', 'u']
#     list_vowels = [letter for letter in letters if letter in vowels]
#     print(list_vowels)
#     result = ''.join(list_vowels)
#     return result

# my_word = input('Enter the word: ')

# print(get_vowels(get_word(my_word)))

# otvet budet
# Enter the word: bootcamp
# ['b', 'o', 'o', 't', 'c', 'a', 'm', 'p']
# ['o', 'o', 'a']
# ooa


# def info(name, age):
#     return f'{name} is {age} years old.'

# print(info('Sam', 19))

# otvet budet Sam is 19 years old.


# def info(name, age):
#     return f'{name} is {age} years old.'

# print(info(age=19, name='Sam'))


# otvet budet Alice is 23 years old.


# def info(name='Sam', age=19):
#     return f'{name} is {age} years old.'

# print(info(age = 23, name = 'Alice'))

# otvet budet Alice is 23 years old.

# def info(name='Sam', age=19):
#     return f'{name} is {age} years old.'

# print(info('John', age = 29))

# otvet budet John is 29 years old.


# def test_func(n1, n2 = 9):
#     return n1 + n2

# print(test_func(n1=10))

# otvet budet 19 


# def create_profile(name, age, image = 'default.jpg'):
#     return name, age, image

# print(create_profile(name = 'Raychel', age = 30, image = 'flower.png'))

# otvet budet ('Raychel', 30, 'flower.png')


#  *args **kwargs


# def func(required, *args, **kwargs):
#     print(required)

#     if args: # True
#         print(args)

#     if kwargs:
#         print(kwargs)

# func('Makers', 'bootcamp', 'Python', name = "Raychel", age = 32)


# otvet budet 
# Makers
# ('bootcamp', 'Python')
# {'name': 'Raychel', 'age': 32}


# def many(*args, **kwargs):
#     print(args)
#     print(kwargs)

# many(1, 2, 3, name = 'Bill', jop = 'It-specialist')

# otvet budet
# (1, 2, 3)
# {'name': 'Bill', 'jop': 'It-specialist'}











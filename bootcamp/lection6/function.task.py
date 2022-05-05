# Video task 1


# def generate_password(param1, param2):
#     import random
#     random_list = random.sample(range(1, 10), k = 7)
#     random_list = [str(i) for i in random_list]
#     password = param1 + param2 + ''.join(random_list)
  
#     return(password)


# def get_info(name = input('Enter you name: '), 
#             last_name = input('Enter your last name: ')):

#     password = generate_password(param1 = name, param2 = last_name)
#     return password

# print(get_info())


# otvet budet 
# Enter you name: Sam
# Enter your last name: Brown
# SamBrown2637581


# Video task 2

# def add(a, b):
#     return a + b

# def substract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def division(a, b):
#     return a / b

# def result(param):
#     return param

# def get_data(action):
#     num1 = int(input('Enter first number: '))
#     num2 = int(input('Enter second number: '))

#     dictionary = {'+': add(num1, num2), 
#                 '-': substract(num1, num2),
#                 '*': multiply(num1, num2),
#                 '/': division(num1, num2)}

#     some_result = dictionary[action]
#     return result(some_result)
# action = input('Select action from list below: + - * /' + '\n')
# print(get_data(action))

# otvet budet 
# +
# Enter first number: 5
# Enter second number: 5
# 10


# Video task 3

# def make_icecream(name, size, **kwargs):
#     print(f'Your {name} icecream {size} size')

#     if kwargs: 
#         print(kwargs)
#         print('Your toppings: ')
#         for value in kwargs.values():
#             print('\t' + value)

# make_icecream(name = 'chocolate', size = 'medium',
#             topping1 = 'peanuts', topping2 = 'coconut')

# otvet budet 
# Your chocolate icecream medium size
# {'topping1': 'peanuts', 'topping2': 'coconut'}
# Your toppings: 
#         peanuts
#         coconut


# task1

# def add(a, b):
#     return a + b

# print(add(2, 5))

# otvet budet 7 

# task 2

# def get_string_length (a):
#     return len(a)

# print(get_string_length('hello'))
# 
# otvet budet 5
#  

# task3

# def get_type(a, b):
#     print(type(a))
#     print(type(b))
# get_type(5, 'a')

# otvet budet 
# <class 'int'>
# <class 'str'>

# task4

# def divide(a, b):
#     return a / b

# print(divide(5, 10)) 

# otvet budet 0.5


# task5

# dict_ = {1: 32, 2: 34, 3: 45}

# def dictionary(dict_):
#     for i in dict_:
#         print(i)
# dictionary(dict_)

# otvet budet 
# 1
# 2
# 3

# task6

# num = 6
# def check(num):
#     if num % 2 == 0:
#         return "It is even number"   
#     else:
#         return "It is odd number"
# print(check(num))

# otvet budet It is even number


# taks7

# def is_palindrome(s: str):
#     snew = s.replace(" ", "").lower()
#     if snew == snew[::-1]:
#         return True
#     return False
# print(is_palindrome('довод'))

# otvet budet true

# task8

# def max_num(*args):
#     return max(*args)
# print(max_num(10, 12))

# otvet budet 12 

# task 9 

# def multiply_list(x):
#     y = 1 
#     for i in x:
        
#         y *= i
#     return y
      
# print(multiply_list([1, 2, 3, 4, 5, 6])) 

# otevet budet 720

#  taks 10

# def sum_digits(num):
#     sum = 0
#     while num > 0:
#         sum += num % 10
#         num //= 10
#     return sum

# print(sum_digits(105))

# otvet budet 6 




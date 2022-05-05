# Decorators - dekoratory eto funkcii kotorye mogut 
# razshyryat funkcional drudoi fukcii ne izmenaia napryamuyu ee logiku

# dekorator - yavlyaetsya patternom proektirovania (programirovania)

# dekorator - eto obertka funkcii

# def hello 

# globals()

# {"hello": <function object>}

# def is_lower(string):
#     if string.islower():
#         return True
#     else:
#         return False

# # print(is_lower(hello))

# some_variable = is_lower
# print(some_variable("Hello world"))

# otvet budet False 


# def func_one():
#     print("Hello")
# # 
# def func_two():
#     func_one()
#     print("World!!!")

# func_two()

# otvet budet 
# Hello
# World!!!


# def generate_even_numbers():
#     return [x for x in range(1, 100) if x %2 == 0]

# def func(kak_ugodno):
#     return kak_ugodno()

# res = func(generate_even_numbers)

# print(res)

# otvet budet 
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

# count_symbol = len
# print(count_symbol("hello world"))

# otvet budet 11 


# ppprint = print

# ppprint("Hello world")

# otvet budet Hello world 


# from  pprint import pprint
# pprint = print

# pprint({"Hello world": 12})

# otvet budet {'Hello world': 12}

# from pprint import pprint

# pprint = print 
# res = dict.fromkeys([x for x in range(1, 100)])
# pprint(res)


# def decorator(func):
#     print("Decorator")
#     func()
#     print("Covered")

# # @decorator
# def some_func():
#     print("I am some Func!!!")

# test = decorator(some_func)  i # @decorator   odno i toje 

# from urllib import request

# def test_docer(func):
#     def wrapper():
#         print("Test decorator obertka nachalo")
#         func()
#         print("Test decorator obertka konec")
#     return wrapper


# def check_time(func):
#     from datetime import datetime

#     def wrapper():
#         start = datetime.now()
#         print(func())
#         func()
#         end = datetime.now() - start
#         print(f"Funkcia {func} Srabotala za {end} sekund")

#     return wrapper

# @test_docer
# @check_time
# def get():
#     import requests
#     resp = requests.get("https://boomerang.kg")
#     return resp

# get()



# def decor(func):
#     def wrapper(data):
#         print("start")
#         func(data)
#         print("end")
#     return wrapper

# @decor
# def some_print(data):
#     return data
# some_print("Test Python Decorator")



# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"{func.__name__} start")
#         func(*args, **kwargs)
#         print(f"{func.__name__} end")

#     return wrapper

# @decorator
# def hello(name):
#     print(f"Hello, {name}")

# hello("Nastya")



       









































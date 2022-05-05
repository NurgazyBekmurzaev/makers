
# video task1


# def title(func):
#     def wrapper(name):
#         name = func(name)
#         return name.title()

#     return wrapper

# def check_symbols(func):
#     def wrapper(name):
#         name_list = list(func(name))
#         print(name_list)
#         symbols_list = list('1234567890!@#$%^&*()+-/<>')
#         name_list = [letter for letter in name_list if not letter in symbols_list]
#         print(name_list)
#         name = ''.join(name_list)
#         return name
#     return wrapper

# @title
# @check_symbols
# def get_name(name):
#     return name

# print(get_name('##$$Sam%%%anta'))

# otvet budet Samanta

# video task2

# def main(iters: int):
#     def actual_decorator(func):
#         def wrapper(*args):
#             print('verhnya bulka')
#             print('pomidory')
#             for _ in range(iters):
#                 print('kotleta')
#             func(*args)
#             print('ketchup')
#             print('salat')
#             print('nijnya bulka')

#         return wrapper
#     return actual_decorator

# customer_choice = int(input('Skolko kotlet vy jelaete? '))
# @main(iters=customer_choice)

# def get_info(*extra_ingredients):
#     if extra_ingredients:
#         for ingr in extra_ingredients:
#             print(ingr)

# ingredients = input('Kakie dopolnitelnye igredienty vy jelaete? perechislite cheres probel ').split()
# get_info(*ingredients)


# otvet budet 
# Skolko kotlet vy jelaete? 2
# Kakie dopolnitelnye igredienty vy jelaete? perechislite cheres probel dfs gf hjk
# verhnya bulka
# pomidory
# kotleta
# kotleta
# dfs
# gf
# hjk
# ketchup
# salat
# nijnya bulka


# task1

# def call_function(func):
#     def wrapper():
#         print(f'Вызываю функцию {func.__qualname__}')
#         func()
#         print(f'Вызов функции {func.__qualname__} прошёл успешно')
#     return wrapper
# @call_function
# def first():
#     print("hello world")
#     return "hello world"
# first()



# task2 
# def func_start_time(func):
#     def wrapper():
#         import datetime
#         time_ = datetime.datetime.now()
        
#         print(f'Функция запущена {time_}')
#         func()
#     return wrapper
# @func_start_time
# def func():
#     print('Hello world')
# func()


# task3

# def make_bold(func):
#     def wrapper():
#         return f'<b>{func()}</b>'
#     return wrapper
# def make_italic(func):
#     def wrapper():
#         return f'<i>{func()}</i>'
#     return wrapper
# def make_underline(func):
#     def wrapper():
#         return f'<u>{func()}</u>'
#     return wrapper
# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return 'Hello world'
 
# print(hello())


# task4

# import time
# def benchmark(func):
#     def wrapper():
#         time_ = time.time()
#         func()
#         print(f'Время выполнения: {time_} секунд.')
#     return wrapper
# @benchmark 
# def fetch_webpage(): 
#     import requests 
#     webpage = requests.get('https://google.com') 
# fetch_webpage()

# task5

# users = {'John':'password_john', 'Jane':'password_jane', 'raychel':'password_raychel'}
# def validate_password(func):
#     def wrapper(username, password):
#         if username in users.keys():
#             if password == users[username]:
#                 func(username, password)
#             else:
#                 print('Password is invalid')
#         else:
#             print('Username is not defined')
#     return wrapper
# @validate_password
# def login(username, password):
#     print(f'Welcome, {username}')
# login('John', 'password_john')

# task6

# def is_admin(func):
#     def wrapper(dict_):
#         res = [value for key, value in dict_.items()]
#         if all(res):
#             res1 = f'Доступ разрешен {res[0]}'
#         else:
#             res1 = f'Доступ запрещен {res[0]}'
#         print(func(res1))
#     return wrapper
# @is_admin
# def get_user(dict):
#     return dict
 
# get_user({'username': 'john133', 'is_admin': True})
# get_user({'username': 'jane133', 'is_admin': False})



# task7

# def route(func):
#     def wrapper(path):
#         url = 'https://www.mywebsite.com/'
#         return url + path
#     return wrapper
# @route
# def get_page(path):
#      return path
 
# print(get_page('about/'))
# print(get_page('products/'))


# task8

# def sort_names(func):
#     def wrapper(list_):
#         list_ = sorted(list_, key=lambda x:x[2])
#         res_name = []
#         for x in list_:
#             if 'F' in x:
#                 res = list(filter(lambda y:str(y).isalpha() and len(y) > 1, x))
#                 res_name.append(f'Ms. {res[0]} {res[1]}')
#             elif 'M' in x:
#                 res = list(filter(lambda y:str(y).isalpha() and len(y) > 1, x))
#                 res_name.append(f'Mr. {res[0]} {res[1]}')
#         return func(res_name) 
#     return wrapper
# @sort_names
# def prefix_name(list_):
#     return list_
# print(prefix_name([('Leo', 'Nimoy', 40, 'M'),
#       ('Carrie', 'Fisher', 35, 'F'),
#       ('Harrison', 'Ford', 38, 'M')]))


# task9

# def get_full_number(func):
#     def wrapper(list_):
#         res = []
#         for x in list_:
#             if x.startswith('0'):
#                 res.append('+996 ' + x[1:4] + ' ' + x[4:])
#             elif x.startswith('+'):
#                 res.append(x[:4] + ' ' + x[4:6] + ' ' + x[6:])
#         func(res)
#     return wrapper
# @get_full_number
# def sort_phone_nums(list_):
#     res = ''
#     for x in sorted(list_):
#         res += x + '#'
#     # res = sorted(res)
#     print(res[:-1])
 
# sort_phone_nums(['0777987456', '0555123456', '0770369852'])


# task10

# def type_check(correct_type):
#     def decorator(func):
#         def wrapper(x):
#             if correct_type is int and type(x) is int:
#                 func(x)
#             elif correct_type is str and type(x) is str:
#                 func(x)
#             elif correct_type is list and type(x) is list:
#                 func(x)
#             elif correct_type is dict and type(x) is dict:
#                 func(x)
#             else:
#                 print('Неверный тип данных :(')
#         return wrapper
#     return decorator
# @type_check(list)
# def func1(word):
#     print(word)
    
# func1([1,2])
# func1([1,2,3,4])

















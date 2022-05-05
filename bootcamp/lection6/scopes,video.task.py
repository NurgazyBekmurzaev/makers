# task 1

# def foo():
#     var = 'переменная foo'
  
#     def bar():
#         global var
#         var = 'переменная foo\nпеременная в foo:  переменная bar'
        
#     bar()
# foo()
# print('переменная в foo: ', var)

# otvet budet 
# переменная в foo:  переменная foo
# переменная в foo:  переменная bar

# task2

# x = 'Я глобальная переменная!'
# def my_func():
   
#     global x
#     print(x)

#     x = 'Я могу изменяться'
#     print(x)

# my_func()
# print(globals())
# otvet budet 
# Я глобальная переменная!
# Я могу изменяться

# taks3

# num = 3
# def mul():
#     global num
#     num = num**2
    
# mul()
# mul()
# mul()
# print(num)

# otvet budet 6561

# task4

# balance = 0
# def get_salary(amount):
#     global balance
#     balance += amount

# def pay_bills(amount, log_name):
#     global balance
#     balance -= amount
#     print(f"Вы заплатили {amount} сом за {log_name}")

# def get_balance():
#     print(f'У вас на счету {balance} сом')

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()

# otvet budet 
# У вас на счету 1000 сом
# Вы заплатили 400 сом за кабельное тв
# У вас на счету 600 сом
# hello@hello-Lenovo-Thi

# task5

# result = 0

# def pow_first(x,y):
#     global result
#     result = x ** y
#     return result

# def pow_second(z):
#     global result
#     result = result % z
#     return result
    
# pow_first(2, 3)
# pow_second(3)
# print(result)

# otvet budet 2 

# taks6

# a = {'Мурат': 24, 
#     'Эржан': 21, 
#     'Чынгыз': 24, 
#     'Алтынай': 17, 
#     'Асема': 16}

# def club():
#   for key, value in a.items():
#         if value < 17:
#             print(f'{key}, извините, Вы не проходите по age-control')
#         else:
#             print(f'{key}, Вы можете войти в клуб')

# club()     
   
# Мурат, Вы можете войти в клуб
# Эржан, Вы можете войти в клуб
# Чынгыз, Вы можете войти в клуб
# Алтынай, Вы можете войти в клуб
# Асема, извините, Вы не проходите по age-control


# taks7

# a = ['pipi', 'papa', 'mama']
# b = []
# def name_capitalize():
#     for x in a:
#         c = x.capitalize()
#         b.append(c)
#     return b
# print(name_capitalize())

# otvet budet ['Pipi', 'Papa', 'Mama']

# task 8

# def count_symbols(x):
#     glasnaya = 0
#     soglasnaya = 0
#     znaki = 0
#     for i in x.lower():
#         if i in 'ауеёиэоыяю':
#             glasnaya += 1
#         elif i in 'йцкнгшщзхъфвпрлджчсмтьб':
#             soglasnaya += 1
#         else:
#             znaki +=1
    
#     return f'Количество гласных: {glasnaya}, согласных: {soglasnaya}, остальных символов: {znaki}'

# print(count_symbols('Мурат супер!'))


# otvet budet  Количество гласных: 4, согласных: 6, остальных символов: 2

# task9

# a = []
# def add_list():
#     for x in range(11):
#         a.append(x)
# add_list()
# print(a)

# otvet budet [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# task 10

# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]

# def numbers(a):
#     for x in a:
#         if x < 7:
#             print(x)

# numbers(a)

# otvet budet 
# 1
# 3
# 4
# 6
# 6
# 0
# 3










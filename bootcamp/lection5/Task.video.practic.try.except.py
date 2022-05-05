# video task 1

# try:
#     num1 = input('Enter anything: ')
#     num2 = input('Enter anything: ')
#     result = int(num1) + int(num2)
# except ValueError:
#     result = num1 + num2
# finally:
#     print(result)

# otvetbudet 
# Enter anything: 7
# Enter anything: 8
# 15

# Enter anything: 5
# Enter anything: makers
# 5makers

# Enter anything: makers
# Enter anything: bootcamp
# makersbootcamp


# video task 2

# dict_ = {1: 'raychel1234', 2: 'johnhello', 3: 'alice-qwerty'}
# dict_ = {value: key for key, value in dict_.items()}
# print(dict_)

# try:
#     username = input('Enter username: ')
#     ID = dict_[username] 
#     print(ID)
# except KeyError:
#     print('There is no such in datebase')
# else:
#     print(f'Welcome, {username}')
# finally:
#     print('Thank you')

# otvet budet 
# Enter username: alice-qwerty
# 3
# Welcome, alice-qwerty
# Thank you

# esli vvedem makers123 otvet budet 
# Enter username: makers123
# There is no such in datebase
# Thank you

# video task 3

# try:
#     age = int(input('Enter your age: '))
#     if age <= 0:
#         raise Exception ('Do not enter negative intergers or zero')
# except ValueError:
#     print('Enter integer, not string')

# else:
#     print(f' Your age: {age}')

# otvet budet 
# Enter your age: 18
#  Your age: 18

# Enter your age: makers
# Enter integer, not string

# Enter your age: -20
# Exception: Do not enter negative intergers or zero


# Practic task1
# try: 
#     some code 1
# except:
#     some code 2
# else:
#     some code 3
# finally:
#     some code 4




# Practic task2

# b = 10
# c = 11
# try:
#     print(a)
# except NameError:
#     print('Vy ne sozdavali peremennuyu a')
 
#  otvet budet 
# Vy ne sozdavali peremennuyu a

# Practic task3

# try: 
#     num1 = int(input())
#     num2 = int(input())
#     result = num1 / num2
# except ZeroDivisionError:                
#     print('На ноль делить нельзя')

# otvet budet 
# 7
# 0
# На ноль делить нельзя

# Practic task4

# try: 
#     num1 = int(input())
#     num2 = int(input())
#     result = num1 + num2
# except ValueError:
#     print('Введите число!')
# else:
#     print(result)

# otvet budet
# 7
# ghg
# Введите число!


# Practic task5

# dict_ = {'key1': 'value1', 'key2': 'value2'}
# try:
#     value = dict_['key3'] 
#     print(value)
# except KeyError:
#     print('Нет такого ключа!')   
    

# otvet budet Нет такого ключа!

# Practic task6

# try:
#     list_ = [1, 4, 9, 16, 25, 36] 
#     print(list_[8])
# except IndexError:
#     print('Нет такого элемента!')

# otvet budet Нет такого элемента!

# Practic task7

# try:
#     age = int(input())
#     if age < 18:
#         raise ValueError('Доступ запрещён')
# except ValueError:
#     print('Введён некорректный возраст')

# else:
#     print('Спасибо')

# finally:
#     print('До свидания!')



# Practic task8

# try: 
#     num1 = int(input())
#     num2 = int(input())
#     result = num1 / num2
# except (ZeroDivisionError, ValueError):                
#     print('Произошла ошибка!')
# else:
#     print(result)


# Practic task9

# cash = int(input())
# if cash < 0:
#     raise ValueError('Сумма не может быть отрицательной!')
# else:
#     print(cash)


# Practic extra task1
# try:
#     inp1 = input()
#     inp2 = input()
#     result = int(inp1) + int(inp2)
# except ValueError:
#     result = inp1 + inp2
# finally:
#     print(result)

# Practic extra task2

# inp1 = input()
# b = inp1.split(' ')
# list_ = []
# for x in b:
#     try:
#         number = int(x)
#         list_.append(number)  
#     except:
#         raise ValueError('Данный элемент не является числом!') 









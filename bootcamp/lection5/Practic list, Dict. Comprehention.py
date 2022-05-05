
# 1 for metod

# list_ = []
# for num in range(1, 21): 
#     list_.append(num * 2)

# print(list_)

# otvet budet 
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]

# 2 list comprehension metod

# list_ = [num *2 for num in range(1, 21)]
# print(list_)

# otvet takje budet 
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]


# list_users = ["Alice", " Sam", "Sandy", "Ben", "John"]
# invitations = ["You are invited " + name for name in list_users]
# print(invitations)

# otvet budet 
# ['You are invited Alice', 'You are invited  Sam', 'You are invited Sandy', 'You are invited Ben', 'You are invited John']

# list1 = [10, 5, -6, -8, -12, 20, 3, 14, 4]
# list2 = [num for  num in list1 if num % 2 == 0 or num % 3 == 0]
# print(list2)

# otvet budet 
#[10, -6, -8, -12, 20, 3, 14, 4]


# strings = ["1998", "2001g", "2008 god", "2020"]
# list_ = [year for year in strings if year.isdigit()]
# print(list_)

# otvet budet ['1998', '2020']

# list_ = ["Raychel", "John", "Alice", "Sam"]
# list_ = [len(name) for name in list_]
# print(list_)

# otvet budet [7, 4, 5, 3]

# list_ = [-5, -12, 0, 1, 2, 8, 4, 5, 7]
# list_ = [x if x < 0 else x ** 2  for x in list_]
# print(list_)

# otvet budet [-5, -12, 0, 1, 4, 64, 16, 25, 49]

# list_ = [-5, -12, 0, 1, 2, 8, 4, 5, 7]
# list_ = [x if x < 0 else x **2 for x in list_ if x % 2 == 0]
# print(list_)

# otvet budet [-12, 0, 4, 64, 16]

# names = ["Raychel", "John", "peter", "jessica", "bill",
#         "steven", "steven 123", "sandy45", "james"]

# filtred_names = [
#     x + "MAKERS" 
#     if len(x) >= 5 
#     else x + "makers" 
#     for x in names 
#     if x.isalpha()
#     ]
# print(filtred_names)

# otvet budet 
# ['RaychelMAKERS', 'Johnmakers', 'peterMAKERS', 'jessicaMAKERS', 'billmakers', 'stevenMAKERS', 'jamesMAKERS']


# names = ["Raychel", "John", "peter", "jessica", "bill",
#         "steven", "steven 123", "sandy45", "james"]

# filtred_names = []
# for x in names:
#     if x.isalpha():
#         if len(x) >= 5:
#             result = x + "MAKERS"
#             filtred_names.append(result)
#         else:
#             result = x + "makers"
#             filtred_names.append(result)
# print(filtred_names)


# otvet takje budet 
# ['RaychelMAKERS', 'Johnmakers', 'peterMAKERS', 'jessicaMAKERS', 'billmakers', 'stevenMAKERS', 'jamesMAKERS']


# john = {"name": "john", "age": 22}
# raychel = {"name": "Raychel", "age": 23}
# peter = {"name": 'Peter', 'age': 17}

# users = [john, raychel, peter]
# ages = [user.get('age', None) for user in users]

# bigger = 0
# smaller = 0
# count = 0
# for age in ages:
#     if age >= 18:
#         bigger += 1
#     else:
#         smaller += 1
#     count += 1

# bigger = bigger * (100/count)
# smaller = smaller * (100/count)
# print(f'Procent polzovatelei s vozrastom bolshe 18: {round(bigger)} procenta')
# print(f'Procent polzovatelei s vozrastom menshe 18: {round(smaller)} procenta')

# otvet budet 
# Procent polzovatelei s vozrastom bolshe 18: 67 procenta
# Procent polzovatelei s vozrastom menshe 18: 33 procenta


# matrix = [
#     [0, 2, 5, 6],
#     [7, 3, 0, 7],
#     [5, 7, 1, 6]
# ]

# ucompress = [n for row in matrix for n in row]
# print(ucompress)

# otvevt budet  [0, 2, 5, 6, 7, 3, 0, 7, 5, 7, 1, 6]

# matrix = [
#     [0, 2, 5, 6],
#     [7, 3, 0, 7],
#     [5, 7, 1, 6]
# ]

# ucompress = []
# for row in matrix:
#     for n in row:
#         ucompress.append(n)

# print(ucompress)

# otvet takje budet [0, 2, 5, 6, 7, 3, 0, 7, 5, 7, 1, 6]

# from datetime import datetime
# from itertools import starmap

# start = datetime.now()

# list_ = []

# for i in range(100000):
#     list_.append(i)

# print(datetime.now() - start)

# otvet budet 0:00:00.012546


# from datetime import datetime

# start = datetime.now()
# list_ = [i for i in range(100000)]

# print(datetime.now() - start)

# otvet budet 0:00:00.005623 bystree vypolnyaet 


# dict_abc = {'a': 1, 'b': 2, 'c': 3}
# dict_123 = {value: key for key, value in dict_abc.items()}

# print(dict_123)

# otvet budet {1: 'a', 2: 'b', 3: 'c'}

# dict_abc = {'a': 1, 'b': 2, 'c': 3}
# dict_123 = {key: value + 2 for key, value in dict_abc.items()}

# print(dict_123)

# otvet budet {'a': 3, 'b': 4, 'c': 5}


# dict_abc = {'a': 1, 'b': 2, 'c': 3}
# dict_123 = {key.upper(): value + 2 for key, value in dict_abc.items()}

# print(dict_123)

# otvet budet {'A': 3, 'B': 4, 'C': 5}



# dict_abc = {'a': 1, 'b': 2, 'c': 3, 'd': -4, 'e': -7}
# new_dict = {
#     key.upper(): value ** 3 
#     for key, value 
#     in dict_abc.items() 
#     if value > 0}
# print(new_dict)

# otvet budet {'A': 1, 'B': 8, 'C': 27}



# a = {'fruits': 
# {'apple': 100, 'orange': 60},
# 'vegetables':
# {'cucumber': 28, 'tomato': 63}
# }

# b = {key: {inner_k: inner_v + 3 for inner_k, inner_v in value.items()} for  key, value in a.items()}
# print(b)

# otvet budet
# {'fruits': {'apple': 103, 'orange': 63}, 'vegetables': {'cucumber': 31, 'tomato': 66}}


# list_ = [-2, 4, -5, 3, -2, 3, 7]
# set_ = {num for num in list_}
# print(set_)


# otvet budet {3, 4, 7, -5, -2} poskolku est' pohojie elementy


# list_ = [-2, 4, -5, 3, -2, 3, 7]
# set_ = {num * 2 for num in list_ if num > 0}
# print(set_)

# otvet budet {8, 6, 14}


# dict_ = {'a': 1, 'b': 2, 'c': 3}
# new = {value **2 for value in dict_.values()}
# print(new)

# otvet budet {1, 4, 9}


# dict_ = {'a': 1, 'b': 2, 'c': 3}
# new = {key.upper() for key in dict_.keys()}
# print(new)

# otvet budet {'A', 'C', 'B'}









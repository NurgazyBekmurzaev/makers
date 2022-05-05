# task 1

# list_ = [new for new in range(1, 101)]
# print(list_)

# task 2

# list_ = [new for new in range(1, 51) if new % 2 != 0]
# print(list_)

# task 3

# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [ num for num in list_ if num % 2 == 0 and num > 0]
# print(int_list)


# task 4

# list_ = [num ** 2 for num in range(1, 26)]
# print(list_)


# taks5 

# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# int_list = [int(num) for num in str_list]
# print(int_list)


# task 6

# list_ = [x if x % 2 != 0 else x ** 2 for x in range(1, 11)]
# print(list_)

# task 7

# list_ = [True if x % 2 == 0 else False for x in range(1, 11)]
# print(list_)

# task 8

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = ['shorter' if len(x)<=4 else 'longer' for x in list_name]
# print(new_list)

# task 9

# dict_ = {num:num**2 for num in range(1,11)}
# print(dict_)

# task10


# n = int(input())
# dict_ = {i if i%n ==0 else i%n == 0 : i**2 for i in range(1, 501)}
# dict_.pop(False)
# print(dict_)


# task 11

# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}

# dict_ = {i: [z for z in range(1, b+1)] for i, b in a.items()}
# print(dict_)

# task 12

# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {i: 'even' if z % 2 == 0 else 'odd' for i, z in dict_.items()}
# print(a)

# task`13`
# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'

# list_ = [num for num in string_.split() if num .startswith('1')]
# print(list_)



# task 14

# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
#  'Olga': {'history': 92, 'math': 96, 'literature': 81},
#   'Nik': {'history': 84, 'math': 85, 'literature': 87}}


# new_dict ={inner_key: [k for k,v in inner_val.items() if v == max(inner_val.values())][0] for inner_key, inner_val in dict_.items()}
# print(new_dict)

# task 15

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {k: v1 for k,v in my_dict.items() for k1,v1 in v.items()}
# print(dict_)


# extra task1

# list_ = range(0, 11)
# list_ = [x / 2 for x in list_ if x % 2 == 0]
# print(list_)


# extra task2

# dict_ = {1: 'one', 2: 'two', 3: 'thre'}

# dict_ = {key: len(value) if key % 2 == 0 else len(value) **3 for key, value in dict_.items()}
# print(dict_)

# otvet budet {1: 27, 2: 3, 3: 64}

# 2 metod

# dict_ = {1: 'one', 2: 'two', 3: 'thre'}

# for key, value in dict_.items():
#     if key % 2 ==0:
#         dict_[key] = len(value)
#     elif key % 2 == 1:
#         dict_[key] = len(value) ** 3 
# print(dict_)

# otvet takje budet {1: 27, 2: 3, 3: 64}

# extra task 3


# set1 = {x for x in range(10)}
# set2 = {y for y in range(7,17)}
# full_set = set1.union(set2)
# raznitsya = set1.intersection(set2) 

# if len(full_set)<20:
#     print(f"В этом сете было {len(raznitsya)} повторения, его длина составляет {len(full_set)}")
# else:
#     print("Ваш объединенный сет полностью уникальный!")







# video task1

# from math import sqrt

# list_ = [4, True, 'makers', 56, 25, 78, 9, False, 89.45, 100]
# new_list = list(map(lambda x: round(sqrt(x)), filter(lambda y: type(y) == int, list_)))
# print(new_list)

# otvet budet [2, 7, 5, 9, 3, 10]

# video task2

# dictionary = [{'name': 'Alice', 'point': 89}, 
#             {'name': 'John', 'point': 59},
#             {'name': 'Sam', 'point': 100},
#             {'name': 'Raychel', 'point': 45}]


# list_ = list(filter(lambda x: x['point'] < 60, dictionary))
# names = list(map(lambda x: x['name'], list_))
# points = list(map(lambda x: x['point'], list_))
# zipped_list = list(zip(names, points))

# expelled_list = list(map(lambda x: f'You are gonna be expelled {x[0]}', zipped_list))


# print(expelled_list)

# otvet budet 
# ['You are gonna be expelled John', 'You are gonna be expelled Raychel']

# video task3

# import functools

# letters = ['m', 'a', 'k', 'e', 'r', 's']
# str_ = functools.reduce(lambda x, y: x + y, letters)
# print(str_)

# otvet budet makers

# taks1

# list_ = [1, 2, 3, 4]  

# result = sum(list_)
# print(result)

# otvet budet 10

# task 2

# list_ = [1, 5, -9, 6, -4] 
# result = all(x > 3 for x in list_)
# print(result)

# otvet budet False 


# task 3

# list_ = [5, 8, 4, 6, 7]
# result = any(x < 0 for x in list_)
# print(result)

# otvet budet False

# task 4

# list_ = [1, 2, 3, 4]  
# result = list(map(lambda x: x ** 2, list_))

# print(result)

# otvet budet [1, 4, 9, 16]

# taks5

# list_ = [1, 2, 3, 4] 
# result = list(filter(lambda x: x % 2 == 0, list_))

# print(result)

# otvet budet [2, 4]

# task6

# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',] 
# result = list(filter(lambda x: len(x) > 7, list_))
# print(result)

# otvet budet ['inheritance', 'polymorphism']

# task7

# import functools
# list_ = [5, 6, 7, 8] 
# result = functools.reduce(lambda x,y: x * y, list_)
# print(result)

# otvet budet 1680


# task8

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
# list2 = list(filter(lambda x: x % 2 == 0, list_))
# list3 = list(filter(lambda y: y % 2 != 0, list_))

# result = f'even: {len(list2)}, odd: {len(list3)}'
# print(result)

# otvet budet even: 5, odd: 5

# task9

# list_ = [-1, 2, 3, 5, -3, 7] 
# result = list(map(lambda x: True if x > 0 else False, list_ ))
# print(result)

#  otvet budet [False, True, True, True, False, True]

# task 10
# import functools
# list_ = ['Paul', 'George', 'Ringo', 'John'] 
# result = functools.reduce(lambda x, y: x if len(x) > len(y) else y, list_)
# print(result)

# otvet budet George










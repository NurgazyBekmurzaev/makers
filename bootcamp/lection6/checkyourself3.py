"""
1) Создайте функцию, которая будет принимать 2 числа, складывать их и возвращать результат сложения.
"""
# def add(): 
#     num1 = 15
#     num2 = 20
#     res = num1 + num2
#     return res
# print(add())



"""
2) Создайте функцию, которая принимает два обязательных параметра. Задача этой функции выводить тип принятых аргументов.
"""

# def get_type(a, b):
#     print(type(a))
#     print(type(b))
# get_type(5, 'a')

"""
3) Напишите функцию, которая принимает список чисел и возвращает их произведение.
"""
# list_ = [1, 2, 3, 4]
# def mulitply(a):
#   count = 1
#   for x in a:
#     count *= x
#   return  count
# print(mulitply(list_)) 



"""
4) Мурат с друзья на выходных решил собратся и пойти в ночной клуб.
Но в ночной клуб пропускают только тех, кому 17+.
Мурату - 24 лет, Эржану - 21 лет, Чынгызу - 24 лет, Алтынай - 17 лет, Асеме - 16 лет.
Напишите программу которая определяет кого пустить в ночной клуб а кого нет.
"""
# def propusk_v_club():
#     age = {'Marat': 24,
#             'Erjan': 21,
#             'Chyngyz': 24,
#             'Altynai': 17,
#             'Asema': 16}

# print(filter(lambda x, y: x if y > 16  else x, propusk_v_club))

# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# def age_control():
#     for key, value in a.items():
#         if value < 17:
#             print(f'{key}, извините, Вы не проходите по age-control')
#         else:
#             print(f'{key}, Вы можете войти в клуб')

# age_control()     

"""
5) Напишите функцию, которая принимает строку и выводит количество гласных, согласных букв и остальных символов. Используйте только кириллические символы
"""

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
#     # print(f'Количество гласных: {glasnaya}, согласных: {soglasnaya}, остальных символов: {znaki}')
#     return f'Количество гласных: {glasnaya}, согласных: {soglasnaya}, остальных символов: {znaki}'
# # cou
# print(count_symbols('Мурат супер!'))




"""
6) Дан списка из чисел. Проверьте, что все числа больше трёх.
"""
# list_ = [2, 4, 5, 6]
# print(all(map(lambda x: x > 3, list_)))


"""
7) Дан список из имён. Найдите самое длинное имя из списка функцией reduce.
"""
# import functools
# list_ = ['John', 'Raychel', 'Aibek']
# result = functools.reduce(lambda x, y: x if len(x) > len(y) else y, list_)
# print(result)











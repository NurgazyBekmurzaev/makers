# Dictionary - slovar - tip dannyh
# slovar eto izmenyaeyi tip dannyh, kotoryi soderjit 
# v sebe para klyuch: znachenie, klyuchom mojet byt tolko neizmenyamyi
# tip dannyh, a znachit vse chto ugodno.
# V drugih yazykah slovar nazyvayutsya po raznomu, naprimer v JS - Object
# v Java associativnyi massiv i vy mojete vstretit slov hesh tablicy.
#  klyuchi doljny byt unikalnymi
#  {"key1": "value1", "key2": "value2"}

# names = {"name1": "John", "name2": "Raychel"}  
# # eto sintakcis dlya dictounary
# # print(names["name1"])
# # print(names["name2"])
# # otvet budet John  Raychel
# some_dict_1 = {}
# some_dict_2 = dict()


# names = {"name1": "John", "name2": "Raychel"}  
# names["name3"] = "Peter"
# print(names)
# otvet budet {'name1': 'John', 'name2': 'Raychel', 'name3': 'Peter'}


# names = {"name1": "John", "name2": "Raychel"}  
# names["name3"] = "Peter"
# names["name1"] = "July"
# print(names)
# otvet budet {'name1': 'July', 'name2': 'Raychel', 'name3': 'Peter'}


# test_dict = {"key": 1, (1, 2):2, True: False, 12.5:3, 12:4}
# print(test_dict)
# otvet budet {'key': 1, (1, 2): 2, True: False, 12.5: 3, 12: 4}

# d = dict(lat="42.121342", long="72.4532543")
# print(d)
# otvet budet {'lat': '42.121342', 'long': '72.4532543'}



# full_information = {
#     "first_name": "John", "last_name": "Snow"
#     }
# full_information["first_name2"] = "John"
# print(full_information)
# # otvet budet {'first_name': 'John', 'last_name': 'Snow', 'first_name2': 'John'}



# hesh tablica - hesh funkcii, hesh value, hesh formula


# dict_ = {"name": "John", "name": "raychel"}
# print(dict_)
# # otvet budet {'name': 'raychel'}


# test = dict()
# print(dir(test))


# .velues --- metod slovarya, kotoraya vozvrashaet vse 
# znachenia klyuchey is slovarya t.e. is dict

# users = {
#     "username": "coderkg",
#     "email": "bestcoderkg@gmail.com",
#     "password": "sdsdfsdfsdfs",
#     "phone_numbers": "+755555",
#     "address": "12 mkr 15",
# }
# values_of_dict = list(users.values())
# print(values_of_dict)
# otvet budet ['coderkg', 'bestcoderkg@gmail.com', 'sdsdfsdfsdfs', '+755555', '12 mkr 15']

#  metod keys 
# users = {
#     "username": "coderkg",
#     "email": "bestcoderkg@gmail.com",
#     "password": "sdsdfsdfsdfs",
#     "phone_numbers": "+755555",
#     "address": "12 mkr 15",
# }
# keys_of_users = users.keys()
# print(keys_of_users)

# otvet budet dict_keys(['username', 'email', 'password', 'phone_numbers', 'address'])


# from datetime import datetime

# posts = []

# title = input("Введите название поста: ")

# if len(title) >= 255:
#     raise ValueError("Недопустимое кол-во символов")

# elif not title[0].isupper():
#     raise ValueError("Название должно начинаться с заглавной буквы!!")

# description = input("Введите описание поста: ")
# hashtags = input("Введите хештеги через пробел в решетках: ").split() 

# for hashtag in hashtags:
#     if not hashtag.startswith("#"):
#         raise ValueError("Неправильный хештег, введите еще раз")

# preview le": title,
#     "description": description,
#     "hashtags": hashtags,
#     "preview": preview,
#     "created_at": created_at,
#     "updated_at": updated_at
# }

# posts.append(post)

# print(posts)


# otvet budet : 

# Введите название поста: Test
# Введите описание поста: Test
# Введите хештеги через пробел в решетках: #svsdvsd
# Выберите картинку: vsvsvs
# [{'title': 'Test', 'description': 'Test', 'hashtags': ['#svsdvsd'], 'preview': 'vsvsvs', 'created_at': datetime.datetime(2022, 3, 9, 1, 55, 10, 63910), 'updated_at': datetime.datetime(2022, 3, 9, 1, 55, 10, 63925)}]

# le": title,
#     "description": description,
#     "hashtags": hashtags,
#     "preview": preview,
#     "created_at": created_at,
#     "updated_at": updated_at
# }

# posts.append(post)

# print(posts)


# otvet budet : 

# Введите название поста: Test
# Введите описание поста: Test
# Введите хештеги через пробел в решетках: #svsdvsd
# Выберите картинку: vsvsvs
# [{'title': 'Test', 'description': 'Test', 'hashtags': ['#svsdvsd'], 'preview': 'vsvsvs', 'created_at': datetime.datetime(2022, 3, 9, 1, 55, 10, 63910), 'updated_at': datetime.datetime(2022, 3, 9, 1, 55, 10, 63925)}]



# methods = {
#     "method1": "append",
#     "method2": "insert",
#     "method3": "pop",
#     "method4": "reverse",
#     "method5": "remove"
# }

# mothed . ged() --- metod ged vozvrashet po klyuchu znachenie i esli takogo klyucha net, 
# to po umolchaniyu vozvrashet None

# res = methods.get("method1")
# print(res)
# # otvet budet append 
# # # ili
# print(methods["method3"])
# # otvet budet pop 
# #  esli 
# res= methods.get("method6")
# otvet budet None

# metod items


# methods = {
#     "method1": "append",
#     "method2": "insert",
#     "method3": "pop",
#     "method4": "reverse",
#     "method5": "remove"
# }

# result = methods.items()
# print(result)
# otvet budet dict_items([('method1', 'append'), ('method2', 'insert'), ('method3', 'pop'), ('method4', 'reverse'), ('method5', 'remove')])
# result= list(methods.items())
# print(result)
# otvet budet ispolzuyu 'list' [('method1', 'append'), ('method2', 'insert'), ('method3', 'pop'), ('method4', 'reverse'), ('method5', 'remove')]


# metod items.() ---eto mnojestvennoe prisvaevanie 
# methods = {
#     "method1": "append",
#     "method2": "insert",
#     "method3": "pop",
#     "method4": "reverse",
#     "method5": "remove"
# }

# for x, y in methods.items():
#     print(x, y)

# otvet budet
# method1 append
# method2 insert
# method3 pop
# method4 reverse
# method5 remove


# a = 15
# b = 20

# a, b = b, a
# print(a, b)

# otvet budet 20 15

# methods = {
#     "method1": "append",
#     "method2": "insert",
#     "method3": "pop",
#     "method4": "reverse",
#     "method5": "remove"
# }

# for key, value in methods.items():
#     print(key, value)
# otvet budet 
# method1 append
# method2 insert
# method3 pop
# method4 reverse
# method5 remove

#  cheres method .pop() mojem vevesti znachenie ukazannogo klyucha
# cars = {
#     "car_1": "Toyota Camry",
#     "car_2": "BMW 525",
#     "car_3": "Mercedes 200",
#     "car_4": "Matiz Daewoo 2010"
# }

# remove_value = cars.pop("car_2")
# print(remove_value)
# print(cars)

# otvet budet
# BMW 525
# {'car_1': 'Toyota Camry', 'car_3': 'Mercedes 200', 'car_4': 'Matiz Daewoo 2010'}



# # Frontend
# username = input("Введите username: ")
# password = input("Введите пароль: ")
# password_confirmation = input("Подтвердите пароль: ")


# db = []

# # Json
# data = {
#     "username": username,
#     "password": password,
#     "password_confirmation": password_confirmation
# }

# password = data.get("password")
# password_confirmation = data.pop("password_confirmation")

# if password != password_confirmation:
#     raise ValueError(
#         "Password and Password confirmation is not match"
#         )
# db.append(data)
# print(db)

# """
# username:
# password:
# """

# otvet budet 
# Введите username: john
# Введите пароль: john123
# Подтвердите пароль: john123
# [{'username': 'john', 'password': 'john123'}]




# Dick comprehension
# List comprehension
# Set comprehension



























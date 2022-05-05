#  if -> elif > else
#  bool -> None ->
# ==, !=, >, <, >=, <=
# or, and, is, in, not in, not


# for, while


# names = ["john", "raychel", "peter"]
# # names[0] eto "john"

# name1 = names[0].capitalize()
# name2 = names[1].capitalize()
# name3 = names[2].capitalize()


# new_names = []
# new_names.append(name1)
# new_names.append(name2)
# new_names.append(name3)
# print(new_names)


# otvet budet ['John', 'Raychel', 'Peter']
# DRY - dont repeat yourself --- ne poftoryat operacii

# names = ["john", "raychel", "peter"]

# range eto  start, and, step

# for x in range(0, 100):
#     print(x)

# for x in range(100, 0, -1):
#     print(x)

# for n in range(1, 100):
#     print(f"{n} +1={n + 1}")


# names = ["john", "raychel", "peter"]

# new_names = []

# for name in names:
#     new_names.append(name.capitalize())
# print(new_names)


#  list -> append, insert(0, "hello"), remove("hello")
            # pop(), index, count, extend([]), sort(), reverse()


# pizza = [
#     "first_item", "second_item", "third_item",
#     "forth_item", "fifth_item", "sixth_item",
# ]
 
# #  count = 1
# for item in pizza:
#     print(f"До сьеденеия куска: , {pizza}")
#     print(f"Сьедаем {item}")
#     pizza.remove(item)
#     print("После сьедения куска: {pizza}")
# print(pizza)

#  fizz  --- esli chislo delitsya na 3 to nujno vyvodit fizz
# buzz ---esli chislo delitsya na 5 to nujno vyvodit buzz
# fizzbuzz --- esli chislo delitsya na 3  i na 5 to nujno vyvodit fizzbuzz


# 3 / 3 == fizz
# 5 / 5 == buzz
# 15 / 3 and 15 / 5 == fizzbuzz


# 100
# for x in range(1, 100):
#     if x % 3 == 0 and x % 5 == 0:
#         print(f"{x} --> Fizz Buzz")
#     elif x % 3 == 0:
#         print(f"{x} --> fizz")
#     elif x % 5 ==0:
#         print(f"{x} --> buzz")
#   otvet budet  
# 3 --> fizz
# 5 --> buzz
# 6 --> fizz
# 9 --> fizz
# 10 --> buzz
# 12 --> fizz
# 15 --> Fizz Buzz
# 18 --> fizz
# 20 --> buzz
#  itd


# phone_numbers = [777, 999, 666, 888, 111, 222, 777, 888, 999] 
# unique_numbers = []

# for x in phone_numbers:
#     if x not in unique_numbers:
#          unique_numbers.append(x)
#     else:
#         continue
# print(unique_numbers)

# #  otvet budet [777, 999, 666, 888, 111, 222]

#  etu zadacju mojno reshit po drugomu

#  set == eto mnojestvo -- tip (struktura) dannyh

# phone_numbers = [777, 999, 666, 888, 111, 222, 777, 888, 999] 
# unique_numbers = list(set(phone_numbers))
# print(unique_numbers)


#  mutable == izmenyaemyi tip dannyh  ---list, dict, set
#  immutable == neizmenyaemyi tip dannyh  --- int, str, tuple, float, frozenset

#  ne izmenyamyi
# str_ = "hello world"
# str_ + "hello"
# print(str_)

#  izmenyaemyi
# list_= ["hello"]
# list_[0] = "world"
# print(list_)

# tuple_ = ("john", "raychel", [])
# tuple_[2]. append('hello')
# print(tuple_)
# otvet budet ('john', 'raychel', ['hello'])

# tuple_ = ("john", "raychel", "john")
# # print(dir(tuple_))
# # print(tuple_.count("john"))
# print(tuple_.index("raychel")) 


# numbers(int, float) - eto tip dannyh neizmenyaemye
# str - eto tip dannyh neizmenyaemye
# tuple - eto tip dannyh neizmenyaemye
# list - eto tip dannyh izmenyaemye
# NoneType - eto tip dannyh neizmenyaemye


# tuple - ()
# list - []
# set - {}

#  metody list
#  removed = [1].pop()

#  Creating Set


# numbers = set()
# names = {"john", "raychel","peter", "jason"}

# for x in names:
#     print(x)

# metod - add

# month = {"Jan", "Februar", "March", "April", "May", "July", "Aug", "Sept", " Oct", "Nov", " Dec"}
# month.add("June")
# print(month)

#  metod - discard, remove

# laptops = {"Acer", "Hp", "Toshiba", " Mac", "Del", "Asus"}
# laptops.discard("Acer") # nahodit Acer i udolyaet, ne doet oshibku esli ne nahodit 
# print(laptops)
# laptops.remove("Hp") # nahodit hp i udolyaet, esli netu to govorit oshibka
# print(laptops)


# laptops = {"Acer", "Hp", "Toshiba", " Mac", "Del", "Asus"}
# removed = laptops.pop() 
# print(removed)
# #  removed -- vozvrashet udalennyi elementy


#  union -- obiedinenie mnojestv

# language_a = {"Python", "JavaScript", "Go"}
# language_b = {"Php", "Java", "C#"}
# all_languages = language_a.union(language_b)
# print(all_languages)
# # otvet budet {'Php', 'Go', 'Java', 'JavaScript', 'Python', 'C#'}

# framework_a = {"Django", "Flask", "FastApi"}
# framework_b = {"aioHttp", "Pyside", "PyQt"}
# all_frameworks = framework_a | framework_b
# print(all_frameworks)
# #  otvet budet {'PyQt', 'Django', 'aioHttp', 'FastApi', 'Pyside', 'Flask'}  znak   | obedinyaet takje kak i union





# x = {1, 2, 3}
# y = {4, 3, 6}
# z = {10, 11, 12}
# data = x.union(y, z)
# print(data)
# # otvet budet {1, 2, 3, 4, 6, 10, 11, 12}


# x = {1, 2, 3}
# y = {4, 3, 6}
# z = {10, 11, 12}
# data = x | y | z 
# print(data)
# # # otvet budet takje {1, 2, 3, 4, 6, 10, 11, 12}



# intersection() - & - peresechenie

# libraries_a = {"requests", "bs4", "python-decouple"}
# libraries_b = {"jinja", "json", "celery"}
# intersections_ = libraries_a.intersection(libraries_b)
# print(intersections_)
# otvet budet set() poskolku netu peresekaemyh elementov



# libraries_a = {"requests", "bs4", "python-decouple", "unitest"}
# libraries_b = {"jinja", "bs4", "celery", "unitest"}
# intersections_ = libraries_a.intersection(libraries_b)
# print(intersections_)
# otvet budet {'bs4', 'unitest'}

# a = {1, 2, 3, 4}
# b = {2, 5, 4, 6}
# c = {10, 11, 12, 2}
# z = a & b & c
# print(z)
# otvet budet {2}

# a = {1, 2, 3, 4}
# b = {2, 5, 4, 6}
# c = {10, 11, 12, 2}
# d = {11, 12, 2}
# z = a.intersection(b, c, d) 
# print(z)
# # otvet budet  takje {2}


# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}
# defference_of_set = set_b.difference(set_a)
# print(defference_of_set)
# otvet budet {8, 6, 7}



# tehnologies_a = {"chrome", "mozilla", "pycharm"}
# tehnologies_b = {"vscode", "facebook", "nano", "pycharm"}
# diff = tehnologies_a - tehnologies_b
# print(diff)
# # otvet budet {'chrome', 'mozilla'}


 

# simetrichnaya raznica
# laptop_a = {"Dell", "Hp", "Acer"}
# laptop_b = {"Mac", "Lenovo", "Asus", "Acer"}
# sym_diff = laptop_a.symmetric_difference(laptop_b)
# print(sym_diff)
# otvet budet {'Dell', 'Mac', 'Asus', 'Hp', 'Lenovo'}


# laptop_a = {"Dell", "Hp", "Acer"}
# laptop_b = {"Mac", "Lenovo", "Asus", "Acer"}
# sym_diff = laptop_a ^ laptop_b
# print(sym_diff)
# otvet takej budet {'Dell', 'Mac', 'Asus', 'Hp', 'Lenovo'}

#  issubset ---   <=   , # issuperset ---   >=  

# set_1 = {"a", "b", "c"}
# set_2 = {"d", "e", "h"}
# subset_check = set_1 <= set_2
# superset_check = set_1 >= set_2
# print(subset_check)
# print(subset_check)


# otvet budet # False # False


# sentence_student = {"I", "am", "Python"}
# sentence_original = {"I", "am", "Python", "Engineer"}
# res = sentence_original.issuperset(sentence_student)
# print(res)
# # otvet budet True 


#  FrozenSet   ne izmenyaemyi tip dannyh, zamorojennyi set
# frozen_ = frozenset([1, 2, 3, 4])
# print(dir(frozen_))


# def union (self, *args):
#     pass
# def add(self, elements: set)
#     pass













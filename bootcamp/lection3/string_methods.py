# count = len('hello world')
# print(count)
# 11



# language = 'Python3'
# print(language[-2])
# n



#  срезы\Slice
# начало:конец:шаг

# new_flavor = 'New Birthday Cake'
# result = new_flavor[0:3]
# print(result)
# New


# var = 'birthday'
# print(var[0:3])
# priny(var[:3])
#  bir одинаковый ответ

# var = 'birthday'
# # print(var[5:8])
# # print(var[5:])
# print(var[-3:8])
# print(var[-3:])
#  day 

# car = 'lamborgigni'
# print(car[:])
# lamborgini

#  начало == 0
# конец == длине строки
# шаг == 1


# car = 'lamborgigni'
# print(car[0::2])
# print(car[0:10:2])
# print(car[:10:2])
# print(car[0:-1:2])
# lmoggi ответ одинаковый на все методы

# car = 'lamborgini'
# print(car[::3])
# lbgi ответ


# flavor = 'birthday cake'
# print(flavor[::-1])
#  результат с конца на начало, т.е заказ, нан и тд

# polindrom_word = input('Введите слово').lower ()
# if polindrom_word == polindrom_word[::-1]:
#     print(f'Да! {polindrom_word} является палиндром')
# else:
#     print(f'Нет! {polindrom_word} не является палиндром')
# vvedite slovo:  zakaz 
# da! zakaz yavlyaetsya polindromom
#  fdfdfdfcvbvsds (net)

#  nahojdenie fragmenta teksta vnutri druogo teksta 
#  metod "find"


# text = 'url of the site: http://boomerang.kg '
# fragment_start_index = text.find('http')
# # print(fragment_start_index)
# #  otvet 17
# fragment_end = text.find(" ", fragment_start_index)
# print(fragment_end)
# # otvet budet 36
# full_url = text[fragment_start_index:fragment_end]
# print(full_url)
# # otvet budet http://boomerang.kg


# text = "hello wait world"
# print(text.find("world"))
#  otvet budet 11 (11 simvol budet w)

# text = "hello wait world"
# res = text.find("w", 7, 15) (naiti "w", nachinat iskat s 7 simvola, iskat do 15 simvola)
# print(res)

#  takje otvet budet 11 (11 simvol budet w)


#  .rfind() --> reverse find

# city = "Bishkek"
# index_of_last_k = city.rfind("k")
# print(index_of_last_k)
#  otvet budet 6 

#  . index()

# city = "New York"
# print(city.index("k"))
# print(city.index("B"))
# #  otvet budet 7 (dlya k), dlya (B) otvet budet (ne naiden)

# revers index -- .rindex() poisk indexa (takje nahodit oshibku esli ne naidet)
# city = "Bishkek"
# print(city.rindex("k"))
# print(city.index("a"))
#  otvet budet 6 dlya (k), dlya (a) otvet budet(ne naiden)

#  .replace()

# city = "Bishkek"
# print(city.replace("k", "K"))
#  otvet budet BishKeK

#  .split()  razdelit po razdelitelyu
# string = "totoro"
# res = string.split("o")
# print(res)
# otvet budet ["t", "t", "r", ""]

# _env = "2121, dfvdfkjdk, dfvsdbsdgb"
# new = _env.split(", ")
# print(new)
#  otvet budet ['2121', 'sdsvsvs', 'dfdddfgdfg']


#  is --> bool value
# .isdigit() -- sostoit li strokka is CIRCUMFLEX

# some_var = "5652"
# print(some_var.isdigit())
# #  otvet budet 'true'

# # isalpha() -- sostoit li stroka is bukv
# name = "john"
# print(name.isalpha())
# otvet budet 'true'

# # isalnum() - sostoit li stroka is cifr i bukv
# num_and_str = "John4343"
# print(num_and_str.isalnum())
# otvet budet "true"

#  .islower() -- sostoit li stroka is simvolov v nijnem registre

# string = "python"
# print(string.islower())
# #  otvet budet true

#  .isupper() -- sostoit li stroka is simvolov v verhnem registre
# language = "DART"
# print(language.isupper())
# #  otvet budet true

#  .istitle() -- tolko "John Snow Black"
#  .upper() - menyaet simvoly na verhnii registr
# .title() -- menyaet pervye 


# name = input("Vvedite imya: ")
# print("Worked upper method")
# print(name.upper())
# print("Worked lower method")
# print(name.lower())
# print("Worked title method")
# print(name.title())
# print("Worked capitalize method")
# print(name.capitalize())
#  opisanie funksii mojno posmotret bloknote

#  . swapcase() -- bolshie bukvy na nijnii a nijnii na verhnie
# name = input("Enter Your Name: ")
# print(name.swapcase())


# S .startswith(str) -- nachinaetsya li stroka "s" s shablona str
# S .endswith(str) --  nachinaetsya li stroka "S" s shablona str

# google_mail = input("type gmail: ")
# if google_mail.endswith("@gmail.com"):
#     print("Successfully saved gmail")
# else:
#     print("Errore, we take only gmail accounts, please check it")
    
# google_mail = input("type gmail: ")
# if google_mail.endswith("#"):
#     print("Successfully saved gmail")
# else:
#     print("Errore, we take only gmail accounts, please check it")



#  . join - sborka stroki is spiska

# my_tuple = ("John", "Raychel", "Peter", "Vicky")
# new_string = "###".join(my_tuple)
# print(new_string)
# #  otvet budet John###Raychel###Peter###Vicky


# udalenie probelnyh simvolov s konca ili s nachalo, ili oboih storon
#  .strip()
# .lstrip()
#  .rstrip()

# name = "     helloworld"
# print(name.lstrip())
# #  otvetbudet s nachalo "helloworld" t.e. s levo


#  task1

# data = input("Vvedite imya, familiu i vozrast cherez probel:\n").split()
# name = data[0]
# last_name = data[1]
# age = data[-1]
# name = name.lower().replace('a', '').title()
# last_name = '*'.join(list(last_name))
# print((name + last_name) * int(age))

# task2

# string = input('Vvedite stroku: ').lower()
# a = string.count('a')
# o = string.count('o')
# i = string.count('i')
# e = string.count('e')
# u = string.count('u')
# y = string.count('y')
# print(f'Vvashei stroke naschitano {a+o+i+e+u+y} glasnyh bukv')

# task3

# username = input('Vvedite user_name: ')
# center = int(len(username)/2)
# new_username = username[:center] + '&' + username[center:]
# password = new_username.swapcase()
# print(f'Vam sgenerirovan parol: {password}')


# string = "Danger"
# letter = string[len(string) //2]
# print(letter)

# name = 'Python'
# version = '3'
# result = "{} - {}, {}.".format(name[0], name, version)
# print(result)
# name = "let" + "hex" + "foo"
# print(name)




















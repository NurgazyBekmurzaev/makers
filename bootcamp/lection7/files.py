
# print(file_)
# print(file_.read())
# print(file_.readable())


# r -  otkrytyie dlya chtenia faila

# w - otkryvat i zapisyvat dannye v fail,
# perezapisyvaet dannye

# x - otkryvaet i zapisyvaet dannye, esli vdrug
# ne nahodit fail, to on vytaskivaet isklyuchenie

# a - otkryvaet i zapisyvaet dannye, esli v faile sushestvuet 
# uje dannye, to on dobavlyaet v konce faile

# b - dlya otkrytia v dvoichnom rejime

# t - otkryvaet tolko v tekstovom rejyme

# + - otkrytie i chtenie i zapis

# name_of_file = "information.txt"

# name = input("Vvedite imya: ")
# address = input("Vvedite adress: ")
# email = input("Vvedite pochtu: ")
# phone_numbers = input("Vvedite nomer telefona: ")
# description = input("Vvedite tekst: ")

# file_ = open(name_of_file, "w")

# file_.write(f"\n{name}\n{address}\n{email}\n{phone_numbers}\n{description}\n")

# file_.write("-"*100)

# otvet budet v novom faile 
# Vvedite imya: JOHN
# Vvedite adress: Californya
# Vvedite pochtu: johnsnow@gmail.com
# Vvedite nomer telefona: +996550332276  
# Vvedite tekst: hello world



# name_of_file = "hello.pdf"

# name = input("Vvedite imya: ")
# address = input("Vvedite adress: ")
# email = input("Vvedite pochtu: ")
# phone_numbers = input("Vvedite nomer telefona: ")
# description = input("Vvedite tekst: ")

# file_ = open(name_of_file, "wb")

# file_.write(f"\n{name}\n{address}\n{email}\n{phone_numbers}\n{description}\n")

# file_.write("-"*100)


# from pprint import pprint


# input pprint
# name_of_file = "Python 18. Schedule - 1 week.pdf"


# file_ = open(name_of_file, "wb")

# file_.write(f"\n{name}\n{address}\n{email}\n{phone_numbers}\n{description}\n")

# file_.write("-"*100)





# from pprint import pprint

# dict_ = dict.fromkeys([x for x in range(1, 6)])
# pprint(dict_)

# otvet budet {1: None, 2: None, 3: None, 4: None, 5: None}



# from pprint import pprint
# import json

# dict_ = {
#         'str': 'Hello world', 
#         'int': '123', 
#         'float': 34.02, 
#         'list': [1, 2, 3],
#         'tuple': (1, 2, 3),
#         'dict': {'a': 1, 'b':2},
#         'bool': True
#         }
# json_file = open('test.json', 'a')

# # load, dump, loads, dumps
# # сериализация - перевод с python в json (dump, dumps)
# # десериализация - перевод с json в python (load, loads)

# json_str = json.dumps(dict_)
# json_file.write(json_str)

# json_file.close()


# with open('test.txt', 'a') as f:
#     f.write('hello')

# otvet budet 'hello' uje v novom faile test.txt


# video razbor Fail

# file1 = open('test.txt','r')
# print(file1.read())
# otkryt i prochitat soderjymoe



# file1 = open('/home/hello/Documents/bootcamp/test_file.txt','r')
# print(file1.read())

# naiti fail i prochitat soderjymoe

# "r" --- reshym tolko chtenie 
# "r+" --- rejym dlya chtenia i zapisi 
# "w" -- rejym dlya zapisi 
#  "w+ " -- rejym dlya zapisi i chtenia 
# "a+" ---- dobovlyaet i chitaet


# file1 = open('test.txt', 'r')
# data = file1.read()
# print(data)

# otvet budet  soderjymoe faila test.txt v vide stroki 



# file1 = open('test.txt', 'r')
# data = file1.read(3)
# print(data)

# esli ukazat simvol to vyidet 3 pervye simvola soderjamia faile test.txt


# file1 = open('test.txt', 'r')
# print(file1.read(4))
# file1.seek(3)
# print(file1.read(6))
# file1.seek(0)
# print(file1.read())

# metod seek pozvolyaet ustonovit kursor na ukazannyi simvol 

# file1 = open('test.txt', 'r')
# print(file1.readline())
# print(file1.readline())

#  metod readline vyvodit postrochno soderjymoe faila

# file1 = open('test.txt', 'r')
# for line in file1:
#     print(line)

# mojno takje cheres cykl proidis i vyvesti kajduyu stroku

# file1 = open('test.txt', 'r')
# list_ = file1.readlines()
# for line in list_:
#     print(line)
# print(list_)

# metod readlines vyvodit soderjymoe v vide spiska

# file1 = open('test.txt', 'r')
# list_ = file1.readlines()
# list_ = [line.replace('\n', '') for line in list_]
# print(list_)

# zamenili simvol \n na pustotu v spiske 


# file2 = open('test.txt', 'w')
# print(file2.write('bootcamp'))

# sozdali fail test.txt i propisali v soderjymoe slovo bootcamp

# file2 = open('test.txt', 'a')
# print(file2.write('bootcamp' + '\n'))

# dopisali slovo bootcamp uje s novoi stroki 



# file2 = open('test22.txt', 'x')
# print(file2.write('bootcamp' + '\n'))

# sozdali novyi fail test22.txt s soderjaniem bootcamp 


# file2 = open('test.txt', 'w')
# file2.write('its such beatiful day today')

# zapisali v fail test.txt dannuyu stroku 

# file2 = open('test.txt', 'w')
# file2.write('its such beatiful day today' + '\n')
# file2.write('Today is my birthday')

# zapisali dva teksta s novoi stroki 
# its such beatiful day today
# Today is my birthday



# file2 = open('test.txt', 'w')
# list_mottos = ["Just do it", "Think different", " because  your worth"]
# list_mottos = [motto + '\n' for motto in list_mottos]
# file2.writelines(list_mottos)

# perezapisali soderjymoe s novoi stroki 
# Just do it
# Think different
#  because  your worth

# file2 = open('test.txt', 'w')
# list_mottos = ["Just do it", "Think different", " because  your worth"]
# list_mottos = [motto + '\n' for motto in list_mottos]
# dict_ = {'name': 'Makers', 'hello': 'world'}

# file2.writelines(dict_)

# peresapisal tolko klyuchi  namehello



# file3 = open('files.txt', 'a')
# list_mottos = ["Just do it", "Think different", " because  your worth"]
# list_mottos = [motto + '\n' for motto in list_mottos]

# file3.write('Mottos of big companies' + '\n')
# for motto in list_mottos:
#     file3.write(motto)

# file3.close()
# print(file3.closed)

# sozdali novyi fail files.txt  cheress 'x' i zapisali 'a' cheres cykl soderjynoe 
# Mottos of big companies
# Just do it
# Think different
#  because  your worth

# with

# with open('files.txt', 'r+') as my_file:
#     print(my_file.read())
#     my_file.write('additional string')

# 'r+' dopisali additional string v fail files.txt 

# with open('files.txt', 'w+') as my_file:
#     print(my_file.read())
#     my_file.write('additional string')

# 'w+' soderjymoe udalilos i zapisalos tolko additional string


# with open('files.txt', 'w+') as my_file:
#     print(my_file.read())
#     my_file.write('additional string')

# print(my_file.closed)


# moduli 

# math, random, datetime 

# import square
# print(square.circle(5))


# from square import circle, triangle, rectangle 
# circle_area = circle(8)
# triangle_area = triangle(9, 6)
# rectangle_area = rectangle(3, 4)
# print(circle_area, triangle_area, rectangle_area)

# otvet budet 201.06 27.0 12













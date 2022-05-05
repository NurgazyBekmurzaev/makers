"""
try: 
    some code 1
except:
    some code 2
else:
    some code 3
finally:
    some code 4
"""

# try:
#     num1 = int(input('Vvedite chislo: '))

# except:
#     print("Vy vveli ne chislo")

# otvet budet 
# Vvedite chislo: iuui
# Vy vveli ne chislo


# try: 
#     num1 = int(input('VVedite pervoe chislo: '))
#     num2 = int(input('VVedite vtoroe chislo: '))
#     result = num1 / num2
# except:                      # goloe isklyuchenie 
#     print('Vy vveli ne chislo')
# else:
#     print(result)
# finally:
#     print('Programma zavershena')

# otvet budet 
# VVedite pervoe chislo: 12
# VVedite vtoroe chislo: 6
# 2.0
# Programma zavershena

# esli vvesti bukvu otvet budet 
# VVedite pervoe chislo: 5
# VVedite vtoroe chislo: g
# Vy vveli ne chislo
# Programma zavershena

# esli vvesti 0 otvet budet 
# VVedite pervoe chislo: 8
# VVedite vtoroe chislo: 0
# Vy vveli ne chislo
# Programma zavershena



# try: 
#     num1 = int(input('VVedite pervoe chislo: '))
#     num2 = int(input('VVedite vtoroe chislo: '))
#     result = num1 / num2
# except ZeroDivisionError:                
#     print(' Na nol delit nelzya')
# else:
#     print(result)
# finally:
#     print('Programma zavershena')
# otvet budet 
# VVedite pervoe chislo: 8
# VVedite vtoroe chislo: 0
#  Na nol delit nelzya
# Programma zavershena


# try: 
#     num1 = int(input('VVedite pervoe chislo: '))
#     num2 = int(input('VVedite vtoroe chislo: '))
#     result = num1 / num2
# except ZeroDivisionError:                
#     print(' Na nol delit nelzya')
# except ValueError:
#     print('Vy vveli ne chislo')
# else:
#     print(result)
# finally:
#     print('Programma zavershena')

# otvet budet 
# VVedite pervoe chislo: 6
# VVedite vtoroe chislo: makers
# Vy vveli ne chislo
# Programma zavershena


# dict_ = dict.fromkeys(('makers', 'bootcamp', 'hello', 'dictionary'), 0)
# dict_ = {key: len(key) for key, val in dict_.items()}
# dict_.update({'except': 'Exception'})

# print(dict_)

# while True:
#     try:
#         key = input('Vvedite slovo: ')
#         if key == 'exit':
#             break
#         dict_[key] += 2 
#         print(dict_)
#     except KeyError:
#         print('Takogo klyucha net v slovare')
#     except TypeError:
#         print('Vy ne mojete provesti konkatenaciyu s chislami')
#     else:
#         print(dict_[key])
#     finally:
#         print(dict_)

#    otvet budet      
# Vvedite slovo: makers
# {'makers': 8, 'bootcamp': 8, 'hello': 5, 'dictionary': 10, 'except': 'Exception'}
# 8
# Vvedite slovo: 4374643763
# Takogo klyucha net v slovare

# Vvedite slovo: except
# Vy ne mojete provesti konkatenaciyu s chislami

# Vvedite slovo: dfdfdfd
# Takogo klyucha net v slovare

# Vvedite slovo: exit

# vyhod iz code 


# dict_ = dict.fromkeys(('makers', 'bootcamp', 'hello', 'dictionary'), 0)
# dict_ = {key: len(key) for key, val in dict_.items()}
# dict_.update({'except': 'Exception'})

# print(dict_)

# while True:
#     try:
#         key = input('Vvedite slovo: ')
#         if key == 'exit':
#             break
#         dict_[key] += 2 
#         print(dict_)
#     except (KeyError, TypeError):
#         print('Dannogo klyucha net libo proizvesti konk-yu s chislami nelzya')
    
#     else:
#         print(dict_[key])
#     finally:
#         print(dict_)
# otvet budet 
# Vvedite slovo: ergeregrge
# Dannogo klyucha net libo proizvesti konk-yu s chislami nelzya


# list_ = [i for i in range(1, 31)]
# try:
#     index = int(input())
#     list_[index] = 'Makers'
# except IndexError:
#     print('You are out of list range')
# except ValueError:
#     print('Please enter the number, not a string')
# else:
#     print("There is no exception")
# finally:
#     print(list_)

# otvet budet     
# 4
# There is no exception
# [1, 2, 3, 4, 'Makers', 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


# try:
#     print(makers)
# except NameError:
#     print('Vy ne sozdavali peremennuyu makers')

# otvet budet  
# Vy ne sozdavali peremennuyu makers

# raise podnimat

# number = int(input('Vvedite chislo ot 1 do 70:  '))
# if not number in range(1, 71):
#     raise Exception('Vy vveli chislo, kotoroe ne nahoditsya v dannom promejutke')
# print('Okey')

# Vvedite chislo ot 1 do 70:  90
# Exception: Vy vveli chislo, kotoroe ne nahoditsya v dannom promejutke














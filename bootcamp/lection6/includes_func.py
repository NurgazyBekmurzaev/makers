
# fstroennye funkcii
# len()  - vytaskivaet dlinnu obiekta
# print() - pechataet v konsol znachenie
# input() - zaprashyvaet dannye 
# divmod() - ostatok ot deleia
# dit()  - vyvodit metody obiekta
# globals() - vyvodit slovar s global dannymi
# locals() - vyvodit slovar s lokalnymi dannymi
# enumerate() - numiruet interiruemye obiekty
# round() - okruglyaet chislo 
# pow() - stepen vyvodit, ostatok ot deleia
# min() - minimalnoe chislo vyvodit
# max() - maksimalnoe chislo vyvodit
# type() - vyvodit tip dannyh obiekta
# id - vyvodit ID obiekta
# range - sozdaet diapozon start:and:step
# sorted - vremenno sortiruet obiekty
# bool - Frue, False
#  



# vstroennaya funkcia abs
# negative = - 125
# absolute = abs(negative)
# print(absolute)

# otvet budet 125

# funcia all()

# list_of_zeroz_num = [0, 1, 2]
# is_true = all(list_of_zeroz_num)
# print(is_true)

# otvet budet False poskolku 0 eto false


# tuple_of_trues_obj = (True, 1, 2, 3)
# is_true = all(tuple_of_trues_obj)
# print(is_true)

# otvet budet True

# def all_(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True

# is_true = all_((True, 1, 2, 3, #0))
# print(is_true)

# otvet budet True, esli dobavit 0 to otvet budet False 


# funcia any

# tuple_of_trues_an_falses = (False, False, True, False)
# print(any(tuple_of_trues_an_falses))

# otvet budet True, poskolku hotyaby esli odin element est True 


# def any_(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False

# print(any_([0, 0, 1]))

# otvet budet True, poskolko est 1 kotoryi True 

#  funcia ascii()

# example_one = ascii([0, 1, 'л'])
# print(example_one)

# otvet budet [0, 1, '\u043b'] bukva л nashel ego kod s ekranirovaniem


# funkcia callable() - cheres etu funciyu mojno proverit na vyzov funcii

# def add(a, b):
#     return a + b

# is_callable = callable(add)
# print(is_callable)

# otvet budet True 




# seasons = ['Spring', 'Summer', 'Fall', 'Whinter']

# res = list(enumerate(seasons, start = 10))
# print(res)

# otvet budet [(10, 'Spring'), (11, 'Summer'), (12, 'Fall'), (13, 'Whinter')]

# name1 = ['John', ' Raychel']
# name2 = ['Peter', 'Jessica']

# for index, value in enumerate(name1):
#     print(value)
#     print(name2[index])
    
    # otvet budet 
# John
# Peter
#  Raychel
# Jessica










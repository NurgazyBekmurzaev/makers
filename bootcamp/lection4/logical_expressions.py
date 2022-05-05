# word = input().lower()

# ru = 'йцукенгшщзхъфывапролджэячсмитьбюё'

# if word == "hello" or word == "привет" or word == "hi":
#     print(word)
# elif word == 'bye' or word == 'пока':
#     print(word)
# else:
#     if word[0] in ru:
#         print("слово не распознано")   
#     else:
#         print("unexpected word")



# num = 5
# if num < 10 and num > 3:
#     print("< 10 and > 3")
# elif num < 10:
#     print("< 0")
# elif num > 3:
#     print("> 10")


# string = input()
# banned = ['бля', 'сука', 'пиздец']
# if banned[0] in string:
#     string = string.replace(banned[0], '*' * len(banned[0]))
# if banned[1] in string:
#     string = string.replace(banned[1], '*' * len(banned[1]))
# if banned[2] in string:
#     string = string.replace(banned[2], '*' * len(banned[2]))
# print(string)


# moms_list = input('мама сказала купить: ').split()
# i_bougth = input('я купил: ').split()
# for item in moms_list:
#     if item in i_bougth:
#         print('молодец, ты купил', item)
#     else:
#         print("Ты забыл", item)
# for item_bougth in i_bougth:
#     if item_bougth not in moms_list:
#         print('Ты зачем купил', item_bougth)


#  dobavleint v spisok

# list_ = [1,1,2,4,5,6,7,1,1,1,1,1,1]
# list_.append(8)
# # print(list_)
# list_.insert(2, 3)
# print(list_)

#  udalenie elementa is spiska
# popped = list_.pop(2)

# # print(list_)

# list_.remove(1)
# print(list_)

#  ochishenenie spiska
# list_ = [1,1,2,4,5,6,7,1,1,1,1,1,1]
# list_.clear()


# podchet odinakovyh elementov
# list_ = [1,1,2,4,5,6,7,1,1,1,1,1,1]
# print(list_.count(5))

#  sortirovka elementov

# list_ = ['b', 'z', 'a', 'd', 'A', 'D', 'Z', '2', '3']
# list_.sort()
# print(('длина списка: '), len(list_))
# print('половина длины: ', len(list_) //2)
# print(list_)
# print(dir(list_))

#  perevaachivaet spisok v obratnuyu storonu
# list_ = ['b', 'z', 'a', 'd', 'A', 'D', 'Z', '2', '3']
# list_.reverse()
# print(list_)


# #  slojeniy elementov
# list_1 = [1,2,3,4,5]
# list_2 = [6,7,8,9]
# # list_3 = list_1 + list_2
# list_1.extend(list_2)

# print(list_1)
# print(list_2)



# print(list_1.index(1))












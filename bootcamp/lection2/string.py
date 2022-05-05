# string
# string methods
#  dir - это функция с помощью которогй можно получить все методы типа данных

# name = "John"
# print(dir(name))


# first_name = input("type your name: ")
# new = first_name.lower()
# print(new)



# salam = "Salam 312"
# print(type(salam))

# hello = 'Hello World!'
# print(type(hello))



# gimn = """Ак мөңгүлүү аска, зоолор, талаалар,
# Элибиздин жаны менен барабар.
# Сансыз кылым Ала-Тоосун мекендеп,
# Сактап келди биздин ата-бабалар!"""
# print(type(gimn))

#  """ стри кавычки можно использовать для содеражания строки """
#  """ кавычки должны быть одинаковыми  с начало и в конце"""



# some_var = "I dont\'t know"
# string_with_screen_one = """Жанна д'Арк ""hello world"" лидером"""

# string_with_screen_one = "Жанна д'Арк \"hello world\" лидером"




#  Форматирование строк \ String interpolation
#  %s бронирование место в строке

# player_1 = 150
# massage = 'Игрок1: %s очков'
# result = massage % player_1
# print(result) 

# in_the_bottom = "Кто проживает на дне океана?"
# yellow = "Желтая губка, малыш без изьяна..."
# always_wins = "Кто побеждает всегда и везде?"
# as_fish = "Кто также ловок как рыба в воде?"

# sponge_bob = "%s --> Спанч Боб Square Pants"
# print(sponge_bob % in_the_bottom)
# print(sponge_bob % yellow)
# print(sponge_bob % always_wins)
# print(sponge_bob % as_fish)




# result = "Я программист %s. Я знаю %s, сейчас изучаю %s"
# print(result % ('крутой', 'puthon', 'javascript'))


# result = "Я программист %s. Я знаю %s, сейчас изучаю %s"
# langs = ('крутой', 'puthon', 'javascript')
# print(result % langs)




# result = "Я программист {2}. Я знаю {1}, сейчас изучаю {0}"
# message = result.format('Java', 'Python', 'Senior')
# print(message)

# Второй способ форматирования с помошью метода .format()

# result = "Я программист {level}. Я знаю {f_lang}, сейчас изучаю {s_lang}"
# message = result.format(f_lang="Python", s_lang="Javascript", level="Senior")
# print(message)


#   третий способ форматирования с помошью метода  f"{}


# name = "John"
# last_name = "Snow"

# hello = f"{name} {last_name} -- the best actor"
# print(hello)




# tytle = "Hello"
# last_tytle = "World"
# result = tytle + " " + last_tytle
# print(result)

# country = "Kyrgystan"
# print(country * 20)

# my_country = "Kyrgystan"
# print(len(my_country))



# string = "makers Bootcamp"
# result = string[7]
# print(result)




# string = "makers bottcamp"
# result1 = string[0:6]  1 вариант
# # result2 = string[:6]  2 вариант
# print(result1)


# string = "makers bottcamp"
# result1 = string[0::2]
# print(result1)

# string = "makers bottcamp"
# result1 = string.split()
# print(result1)

# string1 = "Makers"
# string2 = 'Bootcamp'
# print(string1, string2)

# string3 = "Maker's Bootcamp"
# print(string3)


# sentence = 'i love maker\'s'
# print(sentence)


# string = "Dear friend, \n\nWelcome to Makers Bootcamp! \nEnjoy yor time here with us!"
# print(string)


# string = """Dear friend, 
# Welcome to Makers Bootcamp! 
# Enjoy yor time here with us!"""
# print(string)


# string = 'This is very long string.\
# The length of string in puthon should not be more than 79 simvols.\
# remember this'
# print(string)

# languages = 'languages:\n\t'
# destription = 'Python: backend language\n\t Javascript: frontend language'
# print(languages, destription)

# loop = 'for i in range(5):\n\tprint(i)'
# print(loop)


# sentence = 'hello\vmakers\vbootcamp'
# print(sentence)


# url = r'https://kaktus/\news\topiks/\read'
# print(url)



# string1 = 'Makers'
# string2 = 'Bootcamp'
# # print(string1 + string2)

# print('I study at ' + string1 + ' ' + string2)



# num1 = '6'
# num2 = '7'
# result = num1 + num2
# print(result)


# string = 'makers'
# print(string * 5)


# string = 'makers'
# print(len(string))



# length = len('john')
# print(length)


# sentence = 'strings are ordered'
# print(len(sentence))
# print(sentence[0])
# print(sentence[5])
# print(sentence[7])
# print(sentence[-1])
# print(sentence[-2])
# print(sentence[18])

"""
[x:y]
"""
# string = 'makers bootcamp'
# # print(string[::-1])
# # print(string[3:5:2])
# # print(string[2::3])
# print(string)


# part_string = string[:3]
# print(string[2:-2])
# print(string[:3])
# print(string[:])
# print(part_string)


# world = 'dream'
# # world[0] = 'c'
# world = 'c' + world[1:]
# print(world)





#  find(string), rfind(string)
# string = 'makers bootcamp boot boot'
# # print(string.find('boot'))
# print(string.rfind('boot'))


#  index(string), rindex(string)
# string = 'makers bootcamp boot boot camp'
# print(string.rindex('camp'))


#  replace(pattern, replace_pattern)

# string = 'makers bootcamp makecamp'
# print(string.replace('camp', 'rock', 1))
# # print(string)



#  split(symbol) -> list
# string = 'makers boot*camp'
# print(string.split('*'))

# full_name = input('enter name and lastname: ').split(',')
# name = full_name[0]
# last_name = full_name[-1]
# print(name)
# print(last_name)


#  isdigit(), isalpha(), islower(), isupper()
#  isspace(), istitle()

# string = '123456'
# print(string.isdigit())

# string = 'makers'
# print(string.isalpha())

# string = '123456dfvdf'
# print(string.isalnum())

# string = 'dfvdf'
# print(string.islower())

# string = 'FFFFF'
# print(string.isupper())

# string = 'dfvdf'   
# """символы не отображаемые пробел, табуляция и тд 
# """
# print(string.isspace())
# """результат будет false
# """
# string = '  \n\t    '  
# print(string.isspace())
# """результат будет true
# """


# string = 'Makers Bootcamp'
# print(string.istitle())
# """
# все слова должны начинатся заглавными буквами
# """

# string = 'The quick brown fox jumps over the lazy dog'
# string1 = string.replace('o', '*')
# print(string1)


# world = 'dream'
# world = 'c' + world[1:]
# print(world)

# name = input().split()
# last_name = input().split()
# age = input().split()
# result = name.replace('a', '')
# result1 = '*'.join(list(last_name))
# print((result + result1) * int(age))
























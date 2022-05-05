# functions  ---   funcii

# def - define

# f(x) = x * 2
# f(4)
# f(8)

# def add(): 
#     num1 = 15
#     num2 = 20
#     res = num1 + num2
#     return res
# print(add())

# otvet buder 35


# db = []
# def save(data):
#     db.append(data)

# save({'key1':15})
# save({'key2':25})
# save({'key3':35})

# print(db) 

# otvet budet [{'key1': 15}, {'key2': 25}, {'key3': 35}]



# def swapcase_str(string):
#     if string.islower():
#         return string.upper()
#     else:
#         return string.lower()

# result = swapcase_str('HELLO')
# print(result)

# otvet budet hello 


# def check_add_email(email):
#     full_email = ''
#     if '@' not in email:
#         full_email = email + '@gmail.com'
#         return full_email
#     return email



# res1 = check_add_email('test1')
# res2 = check_add_email('test1@gmail.com')
# print('First: ', res1)
# print('Second: ', res2)

# otvet budet 
# First:  test1@gmail.com
# Second:  test1@gmail.com


# def get_even_num(num):
#     even_nums = []
#     for x in range(1,num):
#         if x % 2 == 0:
#             even_nums.append(x)
#         else:
#             continue
#     return even_nums

# res1 = get_even_num(10)
# res2 = get_even_num(5)
# res3 = get_even_num(15)

# print('First: ', res1)
# print('Second: ', res2)
# print('Third: ', res3)

# otvet budet 
# First:  [2, 4, 6, 8]
# Second:  [2, 4]
# Third:  [2, 4, 6, 8, 10, 12, 14]


# db_users = ['John', 'Raychel', 'Jessica', 'Peter']
# def login_required(username):
#     if username not in db_users:
#         print('Vy ne voshli v acount!!!')
#         username = input('Login: ')
#         return login_required(username)
#     else:
#         return 'Vy uspeshno voshli v acount'

# res = login_required('Aibek')
# print(res)

# otvet budet 
# Login: John
# Vy uspeshno voshli v acount

# def add(num1, num2):
#     return num1 + num2

# def substract(num1, num2):
#     return num1 - num2

# def divide(num1, num2):
#     try:
#         return num1 / num2
#     except ZeroDivisionError:
#         print("You can't divide to zero number!!!")

# def multiple(num1, num2):
#     return num1 * num2

# def main():
#     try:
#         num1 = int(input("Enter the first num: "))
#         num2 = int(input("Enter the second num: "))
#     except ValueError as error:
#         print(error)
#         return main()
#     operator = input("Choose the operator: +/*-: ")
#     res = None
#     if operator == '-':
#         res = substract(num1, num2)
#     elif operator == '+':
#         res = add(num1, num2)
#     elif operator == '/':
#         res = divide(num1, num2)
#     elif operator == '*':
#         res = multiple(num1, num2)
#     else:
#         print("I don't understand your operator symbol!!!")

#     print(res)
#     question = input("Do you want to continue operation? Yes or No: ")
#     if question.lower() == 'yes':
#         return main()
#     else:
#         return 

# main()


#  parametry - my ukazyvaem ih v nachale sozdanii vnutri skobok
#  argumenty - my kogda zapuskaem peredaem argumenty vmesto parametrov

#  imenovannye argumenty - {}
#  pozicionnye argumenty - ()

#  Parametry po umolchaniyu (default)

#  My mojem peredat v funkciyu neogranichennoe kol-vo argumentov (OZU)
#  ili ogranichenie my mojem sami sdelat


# def generate_name(name): # parameters
#     # ....
#     pass

# generate_name('John') # agrument



# def some_func(a, b, c, d):
#     print(a, b, c, d)
# some_func(1, 2, 3, 4)

# # otvet budet 1 2 3 4


# def some_func(a, b, c, d):
#     print(a, b, c, d)
# some_func(b=2,c=3, d=4, a=1)

# otvet takje budet 1 2 3 4



# def some_func(e, a, b, c, d):
#     print(a, b, c, d)
# some_func('12', b=2,c=3, d=4, a=1)

# otvete budet 1 2 3 4



# def add(num1, num2=12):
#     print(num1 + num2)

# add(15)

# otvet budet 27

# def add(num1=15, num2=12):
#     print(num1 + num2)

# add()
# otvet budet 27

# def some_func(*args, **kwargs):
#     print(args, kwargs)

# some_func(12, 14, 15, 16, a='hello', b='world')


# otvet budet (12, 14, 15, 16) {'a': 'hello', 'b': 'world'}

# * --  eto kortej
# ** -- eto slovar
# 
# 


# def name_of_func(param1, param2):
#     print(param1 + param2)
#     return param1 - param2 

# result = name_of_func(4, 3)
# print(result)

# # otvet budet 7 i 1 











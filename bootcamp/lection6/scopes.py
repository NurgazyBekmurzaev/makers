# LEGB = Local      Enclosed   Global       Built-in
    #    Локальные  Замкнутые  Глобальные   Встроенные 


# globals()   vozvrashayut nam slovar
# locals()    vozvrashayut nam slovar



# this_vas_is_visible = ('can be seen inside and outside function')

# def var_visibility():
#     this_is_not_visible = 'cannot be seen outside function'
#     return

# print(this_vas_is_visible)
# print(this_is_not_visible)

# otvet oshibka poskolku this_is_not_visible nahoditsya v lolanoi chasti

# def func(a, b): # parametr
#     return a + b

# res = func(12, 14) # argument
# print(res)


# def some_func(name):
#     print(locals())

# some_func('Asus')

# otvet budet {'name': 'Asus'}


# name = 'Asus'
# def get_name():
#     name = 'Acer'

# get_name()
# print(name)

# otvet budet Asus, poskolku on na globalnoi chasti

# name = 'John'

# def get():
#     name = 'Raychel'
#     print(locals())
# get()
# print(locals())

# otvet budet {'name': 'Raychel'}
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f2d05fa04c0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/hello/Documents/bootcamp/lection6/scopes.py', '__cached__': None, 'name': 'John', 'get': <function get at 0x7f2d05e49e50>}


# name = 'Lenovo'
# def func_one():
#     name = 'Asus'

#     def func_two():
#         name = 'Aser'
#         print(name)
#     func_two
# func_one()


# LEGB = Local      Enclosed   Global       Built-in
    #    Локальные  Замкнутые  Глобальные   Встроенные 

# metod globals()   vozvrashayut nam slovar
# metod locals()    vozvrashayut nam slovar

# for x in range(1, 100):
#     if isinstance(x, str):
#         break
#     else:
#         continue
# print(x)

# otvet budet 99 


# str_ = 'hello'
# if str_ == 'Hello':
#     name = 'John'
# else:
#     name = 'Defoalt'
# print(name)

# for   i   if    sozdayutsya v globalnoi oblasti

# global
# nonlocal

# names = {}
# def func():
#     global names
   
#     names['key'] = 'John'
# func()

# print(names)

# otvet budet {'key': 'John'}


# a = 1
 
# # Uses global because there is no local 'a'
# def f():
#     print('Inside f() : ', a)
 
# # Variable 'a' is redefined as a local
# def g():
#     a = 2
#     print('Inside g() : ', a)
 
# # Uses global keyword to modify global 'a'
# def h():
#     global a
#     a = 3
#     print('Inside h() : ', a)
 
# # Global scope
# print('global : ', a) #1
# f() #--> Inside f(): 1
# print('global : ', a) 
# g()  #--> Inside g(): 2
# print('global : ', a)
# h() #--> Inside h(): 3
# print('global : ', a)

# def func_one():
#     x = 'John'
#     def func_two():
#         nonlocal x
#         x = 'Raychel'
#         print('First: ', x)
#     func_two()
#     print('Second', x)

# func_one()

# otvet budet 
# Furst:  Raychel
# Second Raychel









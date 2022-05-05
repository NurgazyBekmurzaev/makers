# """ Tipy dannyh v python """

# '''1. Immutble - neizmenyaemye '''
# # str, int, float, tuple, frozenset, bool, None

# '''2. Mutble - izmenyaemye'''
# #  list, dict, set 



# """ NUmbers"""  -- chisla

# #  numbers - chisla --- ne izmenyaemyi tip dannyh, prednaznachennyi dlya
# #  hranenia chislovyh znachenii b provedenia nap nimi arifmeticheskih vycheslenie

# #  numbers  - int(chelochislennye)
# #           - float(veshestvennye, drobnye, c plavayushei tochkoi)
#             # - decimal (drobnye, no bolee tochnye)
#             # - complex (kompleksnye 6+6j-3i) 
#             # - long (ogromnye chisla) 

# ''' int, float'''

# abs(int)
# abs(float)
# #  abs - vozvrashaet modul chisla (is otrichatelonogo v polojitelnye), vsegda budet polojitelnoe chislo

# pow(num, degree, remainder) - (num ** degree) % remainder
# #  pow(int, int) - vozvodit pervoe chislo v stepen vtorogo
# # pow(int, int, int) - vozvodit pervoe chislo v stepen vtorogo i nahodit ostatok ot delenia rezultata na tretie chislo

# divmod(num1, num2, remainder) - (num1 // num2), (num1 % num2)
# # divmod(int, int) - vozvrashaet 2 rezultata
# # 1. chastnoe etih chisel
# # 2. ostatok ot delenia etih chisel 

# """Strings""" - stroka
# # stroka erto - neizmenyaemyi tip dannyh, kotoryi predstavlyaet 
# # soboi uporyadochnuyu posledovatelnost simvolov, zaklyuchennyh v dvoinye ili odinarnye kavychki

# #  sintaksiz stroki:
# 'Hello', "Hello", '''mnogostrochnaya stroka s odinarnymy kavychkami''', 
# """ mnogostrochnaya stroka s dvoinymi kavychkami"""

# "hello" * 3 -- "hellohellohello" mojem umnojyt stroku


# # itdexy - numeracia simvolov v uporyadochennoi posledovatelnosti
# # (indeksacia nachinaetsya s nolya)
# "h e l l o   w o r l d"
#  0 1 2 3 4 5 6 7 8 9 10
#               itd -2 -1    
# string = "some string" 
# string[index]                       

# #  srezy - eto chast stroki(podstroka)
# string = "some string"
# string[start:end:(step)]

# # start - nachalo sreza (kokoi cimvol budet pervyi v podstroke)
# # end - konec sreza (do kakogo indeksa srez, simvol pod etim indexom ne vklyuchaetsya)
# # step - shag sreza (cheres skolko indeksov budet sleduyushim simvolom)

# #  kogda srezy s polojytelnymi chislami:
# # start < end

# dir(obj) - spisok vseh metodov u obiekta

# """bool"""
# #  bool - logicheskii tip dannyh, s dvumya znacheniami, ispolzuetsya v usloviah
# # True - (pravda)
# # False - (loj')

# bool([3, 4, 5]) -- True
# bool([False]) -- False
# bool([[]]) - True

# """List"""
# # spiski - imenyaemyi, uporyadochnyi tip dannyh, kotoryi hranit v sebe 
# # posledovatelnost elementov. elementami spiska mogut byt absolyutno 
# # lyubye tipy dannyh, v tom shisle i spiski

# # sintazsiz spiska
# list_ = [1, 'str_', 3.4, (5,3), ['str_', 6]]
# list2 = list( ([1, 'str_', 3.4, (5,3), ['str_', 6]) )
# list3 = ["a"]*6  -----  ["a", "a", "a", "a", "a", "a"]
# list4 = list(range(10))

# # range(start, end, step) - funkcia kotoraya sozdaet posledovatelnost chisel
# #  list(range(5)) - [0, 1, 2, 3, 4] poluchim
# # list(range(2, 8)) - [2, 3, 4, 5, 6, 7]
# # list(range(4, 10, 2))  - [4, 6, 8]
# # list(range(4, 8, 0.1)) - vyidet oshibka, poskolku shag doljen byt celoe chislo

# # len(obj) - funkcia vozvrashayushaya dlinnu obiekta
# #  len(['hello']) - vyidet 1, hranitsya tolko 1 obiekt
# # len('hello') - vyidet 5 poskolku 5 simvolov

# """ Tuple""" - kortej
# # kortej - neizmenyamyi, uporyadochnyi tip dannyh, kotoryi hranit v sebe 
# # posledovatelnost elementov. elementami spiska mogut byt absolyutno 
# # lyubye tipy dannyh, v tom shisle i spiski, i kortejy

# # sintaksiz tuple
# # (1, 2, 3, 4, 5)
# # (3, ) 
# a = (3)  - 3  (int)
# b = (3,)  - (3,) (tuple)
# print(a, b)
# poluchim 3 i (3,)

# """Set"""  -  mnojestva

# # mnojestva - izmenyaemyi, neuporyadochennyi tip dannyh, kotoryi
# # hranit v sebe tolko unikalnye neizmenyaemye znachenia
# # 
# sintaksiz: {1, 2, 3, 4}
# set(iterable)
# print({1, 0, True, False, None, (1, 3)})


# """Frozenset""" - neizmenyaemoe mnojestvo
# # neizmenyaemoe mnojestvo - neizmenyaemyi neuporyadochennyi tip dannyh, kotoryi
# # hranit v sebe tolko unikalnye neizmenyaemye znachenia

# sintaksiz:
# frozenset(iterable)
 
# """Dict""" - slovar
# # slovar - imenyaemyi, neuporyadochennyi tip dannyh, v kotorom hranyatsya
# # nabory pary v vide klyuch:znachenie

# # klyuch v slovare - lyuboi neizmenyaemyi tip dannyh, kajdyi klyuch unikalnyi
# # znachenie v slovare - lyuboi tip dannyh
# # klyuch ot znachenia otdelyaetsya dvoetochiem
# # pary otdelyayutsya zapyatymi

# sintaksiz:
# {"key":"value", 5:["hello"]}
# dict_(iterable)
# dict_([("key1", "value"). ("key2", "value")])


# """None""" 
# # None - neizmenyaemyi tip dannyh, kotoryi ispolzuetsya dlya oboznachenia 
# # pustogo znachenia ili otsutstvia znachenia








# """Conditions""" - uslovia
# # uslovia - operator, kotoryi pozvolyaet nam vypolnyat ili ne vypolnyat 
# # kokoito kusochek koda, kotoyi nahoditsya v tele uslovia.

# sintaksiz:
# if uslovie:
#     telo

# if True:
#     print("uslovie vernoe")

# # takje my mojem sozdovat konstrukcii iz uslovnyh operatorov

# if uslovie:
#     telo1
# elif uslovie:
#     telo2
# else:
#     telo3

# # esli pervoe if uslovie vydalo True, to vypolnitsya telo1
# # esli v pervom if uslovie vydalo False, to proveryaetsya vtoroe uslovie elif
# # esli vtoroe uslovie elif uslovie vydalo True, to vypolnitsya telo2
# # esli vtoroe elif uslovie vydalo False, to vvypolnyaetsya telo3


# #  if i else v konstrukcii mojet byt ispolzovano tolko 1 raz, elif mnogo raz mojet byt ispolzovano

# """Ternarnye uslovia"""
# # ternarnye uslovia - eto uslovie napisannoe v odno stroku

# sintaksiz:
# # telo1 if uslovie else telo2

# # uslovie vernoe if uslovie else uslovie ne vernoe

# """loops""" - cykly

# # cykly - blok koda, kotoryi budet vypolnyatsya neskolko raz

# """For"""
# # for - cykl. kotoryi proizvodit iteracii nad posledovatelnostyu (list, dict, set, str, tuple)

# #  v cykle For my mojem vypolnyat razlichnye operacii nad kajdym elementov posledovatlnosti

# sintaksiz:
# # for element in posledovatelnost:
#     # kakieto deistvia

# """While"""

# while  -  cykl kotoryi 

# while uslovie:
#     kakieto deistvia

# """Comprehensions"""

# # generator posledovatelnosti - specialnaya konstrukcia, 
# # s pomoshyu koroi mojno sozdavat posledovatelnosti

# sintaksiz:
# # deistvie for element in posledovatelnos if uslovie


# [x for x in range(1, 11) if x % 2 == 0]

# ["chetnoe" if x % 2 == 0 else "nechetnoe" for x in range(1, 11)]

# # dlya dict comprehensiont v deistvii doljna byt para (klyuch:znachenie)
# {x:x**2 for x in range(1, 11) if x % 2 == 0}


# init_dict = {"key1": "value1", "key2": "value2"}
# res = {v:k for k,v in init_dict.items()}

# """Try-exept"""

# # try-except - konstrukcia, dlya obrabotki isklyuchenii i oshibok
# # sintaksicheskie oshibki my ne mojem obrabotat

# sintaksiz:
# try:
#     kod, kotoryi mojet vyzvat oshibku
# ecxept isklyuchenie:
#     kod, kotoryi rabotaet, esli oshibka vyshla

# else:
#     kod kotoryi rabotaet, esli oshibka ne vyshla

# finally:
#     kod, kotoryi rabotaet v lyubom sluchae 


# try:
#     raise Exception()
# except:
#     print('ecxeption catched')
# finally:
#     print('finally')



# """Functions"""

# # Funkcii -  imennovannyi blok koda, vypolnyayushii kakieto deistvia i 
# # vozvrashayushii kakoito rezultat. My mojem vyzyvat funkciyu, 
# # obrashayas k nei po imeni i ispolzuya kruglye skobki.

# #  kod kotoryi napisan vnutri funkcii budet rabotat tolko pri vyzove funkcii 
# #  funksii mogut prinimat dannye

# #  paramtry funkcii ---- eto lokalnye peremennye, 
# # kotorym prisvayuvayutsya znachenia pri vyzove funkcii 

# # arfument funkcii --- eto konkretnye znachenia, 
# # kotorye my peredaem v parametry funkcii 

# # def - instrukcia, s pomoshyu kotoroi opredelyaetsya funkcia
# # retern - instrukcia, s pomoshyu kotoroi funkcia vozvrashaet rezultat,
# # # esli ee ne propisat, po defoltu vozvrashaetsya znachenie None

# """Types of arguments"""
# #  pozicionnye argumenty
# # imennovannye argumenty
# # parametry s defoltom
# # neobyazatelnye argumenty (*)
# # klyuchevye argumenty (**)

# def func(pozicionnye, s defoltom, *args, **kwargs):
# args - tuple
# kwargs - dict

# func(pozicionnye,  neobyazatelnye argumenty, parametr = znachenie, klyuch:znachenie)



# """vstroennye funkcii"""

# """map"""

# # map - vstroennaya funkcia, kotoraya vypolnyaet deistvie 
# # nad kajdym elementom posledovatelnosti 
# # i vozvrashet generator novoi posledovatelnosti.
# # ona  prinimaet 2 argumenta:
# # 1  - funkcia, kotoraya prinimaet 1 argument
# # 2 - posledovatelnost

# sintaksiz:
# map(int, ['1', '2', '3', '4'])

# list_ = ['1', '2', '3', '4', '5']
# print( [int(x) for x in List_])
# print(list(map(int, list_)))

# # otvet budet 
# # [1, 2, 3, 4, 5]
# # [1, 2, 3, 4, 5]

# def myfunc(elem):
#     return elem.upper()

# map(myfunc, ['hello', 'world'])
# otvet budet ['HELLO', 'WORLD']



# """Filter"""
# # filter - eto funkcia kotoraya vozvrashaet posledovatelnost
# # iz elementov, sootvetstvuyushih usloviyu
# # ona  prinimaet 2 argumenta:
# # 1  - funkcia, kototraya prinimaet 1 argument i 
# kotoraya vozvraeshaet bulevoe znachenie (esli True, to dobovlyaetsya)
# # 2 - posledovatelnost

# sintaksiz:
# def myfunc(elem):
#     return elem.isalpha()
# print(list(filter(myfunc, ['1', '2', '3', '4', 'd', 's'])))

# # otvet budet ['d', 't']

# def myfunc(elem):
#     if elem > 0:
#         return True
#     return False 
        
# print(list(filter(myfunc, [-1, 4, -6, 0, 8, 30, -2])))
# otvet budet [4, 8, 30]


# """zip"""
# zip - eto funkcia, kotoraya obiedinyaet elementy is 
# neskolkih posledovatelnostei po indexam v tuple, t.e.
# vse elementy pod indexom 0 v pervyi tuple, vse elemety 
# pod indexom 1 vo vtoroi tuple, i t.d.

# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd']
# list3 = [1.0, 2.0, 3.0,]
# print(list(zip(list1, list2, list3)))

# otvete budet [(1, 'a', 1.0), (2, 'b', 2.0), (3, 'c', 3.0)]

# """Reduce"""
# reduce - funkcia, kotoruyu nado importirovat is biblioteki functools 
# from functools import reduce

# ona prinimaet 2 argumenta:
# 1. funkciya, kotoraya prinimaet 2 argumenta
# 2. posledovatelnost

# funkcia reduce beret is posledovaetlnosti 2 elementa, 
# otpravlyaet ih v funkciyu. rezultat i sleduyushii element 
# is posledovatelnosti snova otpravlyaet v funkciyu i t.d. 

# sintaksis:

# from functools import reduce

# def myfunc(x, y):
#     return x if len(x) >= len(y) else y

# res = reduce(myfunc, ["hello", "world", "makers"])
# print(res)
# otvet budet makers


"""Lambda"""

#  lambda - eto anonimnaya funkcia

# sintaksis
# lambda peremennye: deistvie
#  
# myfunc = lambda x: x**2
# print(myfunc(5))

# # otvet budet 25
# myfunc = lambda x, y: x/y
# print(myfunc(5, 6))
# otvet budet 30 

# myfunc = lambda x, y: (x**2, y**2)
# print(myfunc(5, 6))

# otvet budet (25, 36)

# print(1, 2, 3, 4, 5, end='#\n', sep=' : ')






















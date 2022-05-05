# task3

# a = {'Jane', 'Eyre', 22}
# a.add("Hello world!")
# print(a)

# task4
# a = {1, 2, 3}
# b = {3, 4}
# a.update(b)
# print(a)

#  task 5

# a = {1, 2, 3}
# a.discard("4") 
# print(a)

# task 6

# a = {1, 2, 3}
# b = a.remove("9")
# print(b)

# taks 7

# a = {1, False, 3}
# a.clear()
# print(a)

# task 8

# a = {4, 6, 100, -45, -6}
# b = {4, 5, -5, -6}
# c = a.intersection(b)
# print(c)

# task 9

# a = {2, 4, 6, 50, -45, -6}
# b = {4, 3, 5, -5, -6}
# c = a.difference(b)
# print(c)

# taks 10

# a = {2, 4, 5,-45, -6}
# b = {4, 3, 5, -5, 2}
# c = a.union(b)
# print(c)

# taks 11

# a = {0, 1, 2}
# b = {0, 1, 2, 3, 34, 5, 8, 13}
# if b.issuperset(a):
#     print("Подмножество!")

# task 12

# a = {0, 1, 2, 3, 34, 5, 8, 13}
# b = {1, 2, 34}
# if b.issubset(a):
#     print("Надмножество!")


# taks 13

# robert = {5, 7, 11, 10, 28}
# kail = {1, 5, 14, 8, 22} 
# merri = {19, 20, 3, 11, 10}
# if robert & kail and robert & merri:
#     print("kail merri")
# elif robert & kail:
#     print("kail")
# elif robert & merri:
#     print("merri")
# else:
#     print("no one")

# task 14

# tilek = {'Dodo', 'ImperiaPizza', 'FreshBox'}
# timur = {'OcakKebab', 'FreshBox'}
# alexander = {'FreshBox', 'KFC'}
# elina = {'Dodo', 'ImperiaPizza', 'FreshBox', 'OcakKebab', 'KFC'}

# print(tilek.intersection(timur, alexander, elina))


# task 15

# ingredients = {"cыр чеддар","грибы", "соус","шпинат"} 
# ingredients.add('помидор')
# print(ingredients)
# ingredients.discard("колбаса")
# print(ingredients)
# ingredients.remove("шпинат" )
# print(ingredients)
# ingredients.add('базилик')
# print(ingredients)
# ingredients.discard("сыр чеддар")
# print(ingredients)
# ingredients.add('сыр моцарелла')
# print(ingredients)

#  extra task 1

# a = [set(), set(), set()]
# b = a[0]
# c = a[1]
# d = a[2]
# inp1 = input()
# inp2 = int(input())
# if inp2 == 1:
#     b.add(inp1)
# else:
#     b.add("default value")
# if inp2 == 2:
#     c.add(inp1)
# else:
#     c.add("default value")
# if inp2 == 3:
#     d.add(inp1)
# else:
#     d.add("default value")
# print(a)

#  extra task 2

# set1 = {x for x in range(10) if x % 2 == 0};
# set2 = {x for x in range(1, 10, 2)};

# if set1.intersection(set2):
#     print('Множества пересекаются!')
# else:
#     print('Множества не пересекаются!')






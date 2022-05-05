# Task 1

# a = {'x': 1, 'y': 2, 'z': 1}
# b = list(a.keys())
# print(b[0])

# Task2 

# a = {'a': 1, 'b': 2, 'c': 1}
# deleted = a.pop('a')
# print(deleted)

# Task3

# a = {'a': 1, 'b': 2, 'c': 1}
# b = {'f': 55}
# c = a.update(b)
# print(a)

# task4
# a = {'a': 1, 'b': 2, 'c': 1}
# a.clear()
# print(a)

# task5

# a = {'a': 1, 'b': 2, 'c': 1}
# b = list(a.keys())
# print(b)

# task6

# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.copy()
# print(b)

# task7
# a = {'a': 1, 'b': 2, 'c': 1}
# for k in a: 
#      print(k)  

# Task 8

# a = {'a': 1, 'b': 2, 'c': 1}
# for x, z in a.items(): 
#      print(z)  

# task 9

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = a.copy()
# for k, v in a.items(): 
#     if v % 2 == 0:
#         b[k] = 2
#     else:
#         continue
# print(b)
       
# task 10

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}

# for k, v in list(a.items()): 
#     if v == None:
#         del a[k]  
#     else:
#         continue
# print(a)

# task11

# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 

# for k, v in a.items():
#     a[k] = v / 5
#     continue
        
# print(a)


# task 12

# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# for k, v in list(a.items()):
#     if v % 2 == 0:
#         del a[k]
#     else:
#         continue
        
# print(a)

# task13

# a = {'a': 1, 'b': 2, 'c': 3} 

# for k, v in list(a.items()):
#     del a[k]
#     a[v] = k
        
# print(a)

# task 14

# a = {'a': 3, 'b': 2}
# b = sum(a.values())
# print(b)

# task15

# a1 = {"a": 1}
# a2 = dict(key = '1')
# a3 = dict.fromkeys(['z', 'y'])


# extra task1
# d = {'a': 10, 'b': 9, 'c': 3}

# result = 1
# for key in d:    
#     result = result * d[key]
# print(result)

# extra task2

# string = "pythonist" 
# a = {}
# for letter in string:
#     a[letter] = a.get(letter, 0) + 1
# print(a)

















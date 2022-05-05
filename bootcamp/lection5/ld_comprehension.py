


# list comprehension  generator spiskov
# dict comprehension  generatov slovarey

# logika cheres cykl budet takim
# even = []
# for x in range(1, 10):
#     if x % 2 == 0:
#         even.append(x)
#     else:
#         continue
# print(even)
# otvet budet [2, 4, 6, 8]

#  logika cheres comprehension takim

# even = [x for x in range(1, 10) if x % 2 == 0]
# print(even)

# otvet takje budet [2, 4, 6, 8]


# ls = [n for n in range(1, 100)]
# print(ls)


# numbers = [2, 4, 6, 8, 10]
# list_ = [x ** 2 for x in numbers]
# print(list_)
# otvet budet [4, 16, 36, 64, 100]


# list_1 = [10, 5, 8, -4, -8, 20, 3, 4]
# list_2 = [x for x in list_1 if x % 2 == 0 and x > 0]
# print(list_2)
# otvet budet [10, 8, 20, 4]


# years = ['1997', '1997 god', '1997g']
# list_ = [year for year in years if year.isdigit()]
# print(list_)

# otvet budet ['1997']

# names = ['JOhn', 'Raychel', 'Peter', 'Jessica']
# count_of_names = [{name: len(name)} for name in names]
# print(count_of_names)

# otvet budet [{'JOhn': 4}, {'Raychel': 7}, {'Peter': 5}, {'Jessica': 7}]


# numbers = [-5, -12, 0, 1, 2, 8, 4, 5, 7, 9]
# new_numbers = [x if x < 0 else x **2 for x in numbers]
# print(new_numbers)

# otvet budet [-5, -12, 0, 1, 4, 64, 16, 25, 49, 81]


# uslovia vetvlenia: for: filtracia


# matrix = [
#     [0, 2, 5, 6],
#     [7, 3, 0, 7],
#     [5, 7, 1, 6]
# ]

# ucompress = [n for row in matrix for n in row]
# print(ucompress)

# otvevt budet  [0, 2, 5, 6, 7, 3, 0, 7, 5, 7, 1, 6]



# dictionary comprehension


# dict_abc = {'a': ord('a'), 'b': ord('b'), 'c': ord('c')}

# dict_ord = {value: key for key, value in dict_abc.items()}

# print(dict_ord)

# otvet budet {97: 'a', 98: 'b', 99: 'c'}



# dict_abc = {'a': {'a': 97}, 'b': {'b': 98}}

# new_dict = {}
# for key, value in dict_abc.items():
#     new_dict[key] = value[key]
# print(new_dict)

# otvet budet {'a': 97, 'b': 98}

# dict_abc = {'a': {'a': 97}, 'b': {'b': 98}}

# new_dict = {key: value[key] for key, value in dict_abc.items()}
# print(new_dict)
# otvet takje budet {'a': 97, 'b': 98}


# dict_ = {1: 1, 2: 2, 3: 3}
# dict_ = {key: list(range(1, value + 1)) for key, value in dict_.items()}
# print(dict_)

# otvet budet {1: [1], 2: [1, 2], 3: [1, 2, 3]}










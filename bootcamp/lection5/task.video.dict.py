# task 1

# university = {
#     "программирование": 150,
#     "экономика": 98,
#     "медицина": 82
# }
# # a
# university["экономика"] = 120
# # b
# # university["лингвистика"] = 56
# # university.update({"лингвистика": 56})
# university.setdefault("лингвистика", 60)
# # print(university)
# print(university.pop("медицина"))
# # print(university)
# print(sum(list(university.values())))

# otvet budet 330

# task 2

# dict_ = {1: "a", 2: "b", 3: "c"}
# new_dict_ = {}
# for key, val in dict_.items():
#     new_dict_.update({val:key})
# print(new_dict_)

#  otvet budet  {'a': 1, 'b': 2, 'c': 3}

# task 3

# count = int(input("how many guest do you want to invite? "))
# guests = {}
# for i in range(1, count+1):
#     name = input("Enter guest name: ")
#     guests.setdefault(i, name)
# print(guests)

# otvet budet 
# how many guest do you want to invite? 5
# Enter guest name: sam
# Enter guest name: john
# Enter guest name: kate
# Enter guest name: bob
# Enter guest name: like
# {1: 'sam', 2: 'john', 3: 'kate', 4: 'bob', 5: 'like'}



# task4

# my_list = [
#     {"potato": 10},
#     {"milk": 1},
#     {"eggs": 20},
#     {"bread": 2}
# ]
# while my_list:
#     product_to_remove = input()
#     for products in my_list:
#         if product_to_remove in products:
#             del products[product_to_remove]
#             print(my_list)
#         # any, all() = or, and
#     if not any(my_list):
#         break

# print("It\'s time to pay")


# otvet budet 
# bread
# [{'potato': 10}, {'milk': 1}, {'eggs': 20}, {}]
# potato
# [{}, {'milk': 1}, {'eggs': 20}, {}]
# milk
# [{}, {}, {'eggs': 20}, {}]
# eggs
# [{}, {}, {}, {}]
# It's time to pay







































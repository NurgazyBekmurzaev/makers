# task 1

# okroshka = {
#     "kartoshka", "yaca", "ogurcy", 
#     "kolbasa", "zelen"
#     }
# olive = {
#     "kartoshka", "solennye ogurcy",
#      "kolbasa", "morkov", "yaca"
#      }
# common = len(okroshka.intersection(olive))
# print(common)

# unigue_okroshka = okroshka.difference(olive)
# unique_olive = olive.difference(okroshka)
# print(unique_olive)
# print(unigue_okroshka)

# task 2

# users = {
#     ("Alice", "Python", 5),("John", "Python", 6), 
#     ("Ann", "JavaScript", 1), ("Alice", "JavaScript", 2), 
#     ("Raychel", "Python", 8)}

# countPython = 0
# countJS = 0
# setPython = set()
# setJS = set()
# for info in users:
#     countPython += info.count("Python")
#     countJS += info.count("JavaScript")

#     if info[1] == "Python":
#         setPython.add(info[0])
#     else:
#         setJS.add(info[0])

# print(countPython)
# print(countJS)
# print(setPython & setJS)


# Task 3


# while True:
#     valuta = (input("Введите валюту (сом или доллар): "))
#     summa = int(input(f"Введите сумму, которую вы хотите перевести в {valuta}ы: "))
#     if valuta == "доллар":
#         result = summa / 84.80
#         print(f"{round(result, 1)} $")
#     elif valuta == "сом":
#         result = summa * 84.80
#         print(f"{round(result, 1)} сом")
#     else:
#         print("Введите правильные данные")
#         continue
#     choice = input("Хотите продолжить?:")
#     if choice.lower() == "да":
#         continue
#     else:
#         print("Всего хорошего")
#         break 
            






























# video task1

# with open('numbers.txt', 'w') as file1:
#     for number in range(1, 21):
#         file1.write(str(number) + '\n')

# with open('squares.txt', 'w') as file2:
#     with open('numbers.txt') as file1:
#         data = file1.read().split('\n')
#         data.pop()
#         print(data)
#         new_data = list(map(int, data))
#         for number in new_data:
#             file2.write(str(number ** 2) + '\n')
   
# video task2

# with open('usernames.txt', 'w') as my_file:
#     while True:
#         username = input('Enter username: ')
#         if username.lower() == 'end':
#             break
#         my_file.write(f'{username} - {len(username)}\n')

# otvet budet 
# john - 4
# alice - 5
# kate - 4
# sam - 3
# emili - 5
# makers - 6
# bootcamp - 8


# task1

# with open('task1.txt', 'r') as file:
#     for line in file.readlines(9):
#         print(line)

# otvet budet 
# 1
# 2
# 3
# 4
# 5

# task2

# with open('task2.txt', 'r') as file:
#     for line in file:
#         print(line)


# otvet budet 
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


# task3

# with open("task3.txt", "w+") as file:
#     for x in range(10):
#         list_ =  (str(x) + "*")
#         file.write(list_)
#     file.seek(0)
#     print(file.read())

# otvet budet 0*1*2*3*4*5*6*7*8*9*

# task4

# with open('task4.txt', 'r') as file:
#     count = 0
#     for x in file:
#         count += 1
#     print(count)

# otvet budet 18

# task 5

# list_ = []
# for x in open('task5.txt'):
#     list_.append(x)

# min_ = min(list_)
# max_ = max(list_)

# with open('task6.txt', 'w') as file_:
#     file_.write(f'{min_}-{max_}')

# otvet budet 1-456 











#  task1

# password = input('Vvedite parol: ')
# if password.isdigit() and len(password) >= 8:
#     print('Vash parol cohranen')

# if not password.isdigit():
#     print('Vash parol doljen hranit tolko chisla')

# if not len(password) >= 8:
#     print('Vash parol doljen soderjat ne menee 8 simvolov')

#  task2

# point = input('Введите свои баллы по математике, английскому языку и литературе через запятую:').split(', ')
# math = int(point[0])
# english = int(point[1])
# litr = int(point[2])

# average = (math + english + litr) / 3

# if average > 69:
#     print(f'Vy dopusheny k egzamenu. Vash srednii ball sostavlyaet {round(average, 1)}')
# else:
#     print('Vy ne dopusheny k egzamenu')


# task3

# import random

# play = ['kamen', 'nojnicy', 'bumaga']
# my_choice = input('vash vybor: ')
# computer_choice = random.choice(play)

# if my_choice == 'nojnicy' and computer_choice == 'bumaga':
#     print(f'Vybor computera: {computer_choice}\nVy vyigrali')
# elif my_choice == 'nojnicy' and computer_choice == 'kamen':
#     print(f'Vybor computera: {computer_choice}\nVy proigrali')
# elif my_choice == 'kamen' and computer_choice == 'nojnicy':
#     print(f'Vybor computera: {computer_choice}\nVy vyigrali')
# elif my_choice == 'kamen' and computer_choice == 'bumaga':
#     print(f'Vybor computera: {computer_choice}\nVy proigrali')
# elif my_choice == 'bumaga' and computer_choice == 'kamen':
#     print(f'Vybor computera: {computer_choice}\nVy vyigrali')
# elif my_choice == 'bumaga' and computer_choice == 'nojnicy':
#     print(f'Vybor computera: {computer_choice}\nVy proigrali')
# elif (my_choice == 'nojnicy' and computer_choice == 'nojnicy') or (my_choice == 'kamen' and computer_choice == 'kamen') or (my_choice == 'bumaga' and computer_choice == 'bumaga'):
#     print(f'Vybor computera: {computer_choice}\nNichya')



import random

name = input('Как Вас зовут?:  ')
print(f'Здравствуйте {name}!')
select = input('Хотели бы сыграть в игру "Угадай число" ?\n напишите Да либо Нет: ')
game = 0
while game == 0:
    num = random.randint(0, 10)
    life = 1
    game2 = 0
    while game2 == 0:
        if select == 'Да' or select == 'да':
            user_num = input('Загадайте число от 0 до 10!: ')
            if user_num.isdigit():
                user_num = int(user_num)
                if num == user_num:
                    print(f'Вы угадали число, использовав {life} попыток.')
                    select = input('Хотите ли вы сыграть ещё раз?\n напишите Да либо Нет: ')
                    game2 = 1
                elif num != user_num:
                    print('Вы не угадали число!')
                    life += 1
            else:
                print('Загадайте число, а не букву!')
        elif select == 'нет' or select == 'Нет':
            print('Игра окончена!')
            game = 1
            game2 = 1
        else:
            select = input('Напишите Да либо Нет! ')


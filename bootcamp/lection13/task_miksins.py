

# task1 
# class Auto:
#     def ride(self):
#         return 'Riding on a ground'
# class Boat:
#     def swim(self):
#         return 'Floating on water'
# class Amphibian(Auto, Boat):
#     ...
# obj = Amphibian() 
# print(obj.ride()) 
# print(obj.swim()) 

# task2

# class RadioMixin:
#     def play_music(self, title):
#         return f'Песня называется {title}'
# class Auto(RadioMixin):
#     ...
# class Boat(RadioMixin):
#     ...
# class Amphibian(Auto, Boat, RadioMixin):
#     ...
# auto = Auto()
# boat = Boat()
# obj = Amphibian()
# print(auto.play_music('hello'))
# print(boat.play_music('hello'))
# print(obj.play_music('hello'))


# task3

# import datetime
# class Clock:
#     def current_time(self):
#         res = datetime.datetime.today().strftime("%H:%M:%S")
#         return res
# class Alarm:
#     def on(self):
#         return 'Будильник включен'
#     def off(self):
#         ...
# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         return super().on()
# clock = AlarmClock()
# print(clock.current_time()) 
# print(clock.alarm_on())

# task4

# from abc import ABC, abstractmethod
# class Coder(ABC):
#     count_code_time = 0
#     @abstractmethod
#     def get_info(self):
#         ...
#     @abstractmethod
#     def coding(self):
#         ...
# class Backend(Coder):
#     def __init__(self, experience, languages_backend):
#         self.experience = experience
#         self.languages_backend = languages_backend
#     def get_info(self):
#         return f'{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'
#     def coding(self, t):
#         self.count_code_time = t
# class Frontend(Coder):
#     def __init__(self, experience, languages_frontend):
#         self.experience = experience
#         self.languages_frontend = languages_frontend
#     def get_info(self):
#         return f'{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'
#     def coding(self, t):
#         self.count_code_time = t
# class Fullstack(Frontend, Backend):
#     ...
# a = Backend('Junior', 'Python')
# b = Frontend('Middle', 'Javascript')
# c = Fullstack('Senior', 'Python and JS')
# a.coding(12) 
# b.coding(45) 
# c.coding(17) 
# print(a.get_info()) 
# print(b.get_info()) 
# print(c.get_info())


# task5

# class Triangle:
#     def __init__(self, height, base):
#         self.height = height
#         self.base = base
#     def get_area(self):
#         res = (self.base * self.height)/2
#         return int(res)
# class Square:
#     def __init__(self, side):
#         self.side = side
#     def get_area(self):
#         res = self.side ** 2
#         return res
# class Pyramid(Triangle, Square):
#     def __init__(self, height, base):
#         Triangle.__init__(self, height, base)
#     def get_volume(self):
#         res = 1/3 * self.base**2 * self.height
#         return res
# triangle = Triangle(15, 12)
# print(triangle.get_area())
# square = Square(15)
# print(square.get_area())
# piramid = Pyramid(12, 13)
# print(piramid.get_volume())

# task6

# class CreateMixin:
#     def create(self, key, todo):
#         if key in self.todos.keys():
#             return 'Задача под таким ключём уже существует'
#         self.todos[key] = todo
#         return self.todos
# class DeleteMixin:
#     def delete(self, key):
#         if key in self.todos.keys():
#             res = self.todos.pop(key)
#         return res
# class UpdateMixin:
#     def update(self, key, new_value):
#         self.todos.update({key:new_value})
#         return self.todos
# class ReadMixin:
#     def read(self):
#         res = [x for x in self.todos.items()]
#         return sorted(res)
# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     def __init__(self):
#         self.todos = {}
#     def set_deadline(self, data):
#         from datetime import date
#         data = data.split('/')
#         dead_line = date(int(data[2]), int(data[1]),

# task7

# class ExtensionMixin:
#     def add_extension(self,desc):
#         self.extensions.append(desc)
#         return f"Добавлено новое расширение {desc} для игры {self.name}."
#     def remove_extension(self,desc):
#         try:
#             self.extensions.remove(desc)
#             return f'{desc} был отключен от {self.name}.'
#         except:
#             return "Такого экстеншна нету в списке."
            
# class Game(ExtensionMixin):
#     def __init__(self,type,name):
#         self.name = name
#         self.extensions = []
#         self.type = type
#     def get_description(self,desc):
#         return f"{self.name} {desc}"
#     def get_extensions(self):
#         if self.extensions == []:
#             return "Нет подключенных расширений"
#         else:
#             res = ""
#             for i in self.extensions:
#                 res += i+" "
#             return res
# mine = Game("RPG","Minecraft")
# print(mine.get_description("это инди-игра в жанре песочницы с элементами выживания и открытым миром."))
# print(mine.add_extension("Multiverse-Core"))
# print(mine.extensions)
# print(mine.remove_extension("Multiverse-Core"))
# print(mine.extensions)
# print(mine.add_extension("GodMode2"))
# print(mine.add_extension("GodMode3"))
# print(mine.get_extensions()



"""
1) Будильник
Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, с методами для включения и выключения будильника.
Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
нему метод для установки будильника, при вызове которого должен включатся будильник.
"""

# class Clock:
#     def vremya(self):
#         import datetime
#         res = datetime.datetime.now()
#         print(res.strftime("%H:%M:%S"))
    
# class Alarm:
#     def vkl(self):
#         print("Budilnik is vkl")
#     def vykl(self):
#         print("Budilnik is vykl")

# class AlarmClock(Clock, Alarm):
#     def budilnik_vkl(self):
#         self.vkl()

# clock = AlarmClock()
# clock.vremya() 
# clock.budilnik_vkl() 
    


"""
2) Напишите класс Student, который описывает студента. 

У студента есть следующие атрибуты: имя, фамилия, класс, и оценки по предметам 
в следующем виде: {math’: 100, ‘history’: 89, literature’: 88}. 
Сделайте так, чтобы сравнение студентов между собой производилось 
по средней оценке студента по предметам.
"""


# class Student:
#     def __init__(self, name, class_name, ball):
#         self.name = name
#         self.class_name = class_name
#         self.ball = ball
    
#     def __lt__(self, other):
#         res_a = 0
#         res_b = 0
#         for x in self.ball.values():
#             res_a += x
#         for x in other.ball.values():
#             res_b += x
#         return f'< {res_a < res_b}'
#     def __gt__(self, other):
#         res_a = 0
#         res_b = 0
#         for x in self.ball.values():
#             res_a += x
#         for x in other.ball.values():
#             res_b += x
#         return f'> {res_a > res_b}'
#     def __le__(self, other):
#         res_a = 0
#         res_b = 0
#         for x in self.ball.values():
#             res_a += x
#         for x in other.ball.values():
#             res_b += x
#         return f'<= {res_a <= res_b}'
#     def __ge__(self, other):
#         res_a = 0
#         res_b = 0
#         for x in self.ball.values():
#             res_a += x
#         for x in other.ball.values():
#             res_b += x
#         return f'>= {res_a >= res_b}'
# obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88})  
# obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 89, 'literature': 88})  
# print(obj_student1 > obj_student2)  
# print(obj_student1 < obj_student2)  
# print(obj_student1 >= obj_student2)  
# print(obj_student1 <= obj_student2)

"""
3) Напишите класс учеников Makers, который будет содержать 4 атрибута: 

- атрибут экземпляра name (имя студента)
- атрибут класса students_count (количество учеников)
- атрибут экземпляра класса language (язык, которому обучается студент)
- атрибут экземпляра класса kpi (оценка студента)

Также класс должен содержать следующие методы:

- метод, который будет создавать нового ученика, и при этом увеличивать количество студентов на 1.
- метод который будет выводит имя и язык, выбранный учеником.
- а также метод, который будет устанавливать оценку ученику.
"""

# class Makers:
#     student_count = 0
#     def __init__(self, name, language, kpi):
#         self.name = name
#         self.language = language
#         self.kpi = kpi

#     @classmethod
#     def new_student(cls, name, language, kpi):
#         cls.student_count += 1
#         return cls(name, language, kpi)
    
#     def get_info(self):
#         return f'Student name: {self.name}, Language: {self.language}'
#     def set_kpi(self, num):
#         self.kpi += num
#         return self.kpi

# student1 = Makers.new_student("Atai", "Pyhton", 0)
# student2 = Makers.new_student("Nuraiym", "JS", 0)
# print(student1.set_kpi(89)) 
# print(student1.get_info()) 
# print(student2.set_kpi(90)) 
# print(student2.get_info()) 
# print(Makers.student_count)



"""
4) Dollar.
Создайте функцию dollarize, которая принимает дробное число (float) и переводит его в
долларизованный формат:

dollarize(123456.78901) -> "$123,456.80"
dollarize(-123456.7801) -> "-$123,456.78"
dollarize(1000000) -> "$1,000,000"

Создайте класс MoneyFmt, который содержит один единственный атрибут amount и 4 метода:
- init - инициализирует значение атрибута amount
- update - задаёт объекту новое значение amount
- repr - возвращает значение float
- str - метод, который реализует логику функции dollarize()

//Вывод должен выглядеть следующим образом:
cash = MoneyFmt(12345678.021)
print(cash) -- выводит "$12,345,678.02"
cash.update(100000.4567)
print(cash) -- выводит "$100,000.46"
cash.update(-0.3)
print(cash) -- выводит "-$0.30"
repr(cash) -- выводит -0.3
"""

# def dollarize(float):
#     if float >= 0:
#         return '${:,.2f}'.format(float)
#     else:
#         return '-${:,.2f}'.format(float)

# class MoneyFmt:
#     def __init__(self, amount) -> None:
#         self.amount = amount
        
#     def update(self, value):
#         self.amount = value


#     def __repr__(self) -> str:
#         return str(self.amount)

#     def __str__(self) -> str:
#         return str(dollarize(self.amount))

# cash = MoneyFmt(12345678.021)
# print(cash) 
# cash.update(100000.4567)
# print(cash) 
# cash.update(-0.3)
# print(cash) 
# repr(cash) 
        

    







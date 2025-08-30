
# class Sword:

#     def __init__(self, name, blade_length, grip, material='сталь'):

#         self.name = name

#         self.blade_length = blade_length

#         self.material = material

#         self.grip = grip

#         self.strength = 10

#         print(f'Новый меч {name} выкован!')

    

#     def slashing_blow(self):

#         self.strength -= 10

#         return (f'Нанесён рубящий удар мечом {self.name}. '

#                 f'Радиус поражения: {self.blade_length}.')


#     def piercing_strike(self):

#         self.strength -= 5

#         return (f'Нанесён пронзающий удар мечом {self.name}. '

#                 f'Рукоять {self.grip} мягко легла в руку.')

#     def sharpen(self):

#         self.strength = 100

#         return (f'Меч "{self.name}" заточен,'

#                 f' {self.material} отлично поддалась обработке.')

    

#     # Вот он — новый метод! Именно в нём описывается то, что должно выводиться

#     # при печати объекта.

#     def __str__(self):

#         # Можно задать любую строку, например

#         # «Не печатай меня, ведь я — объект!».

#         # Но лучше пусть при печати выводится что-то осмысленное,

#         # например имя объекта и его основные параметры.

#         return (

#             f'Меч — «{self.name}». ' 

#             f'Выкован из материала {self.material}, '

#             f'длина клинка — {self.blade_length}, '

#             f'прочность — {self.strength}.'

#         )

# katana = Sword('Верный', 1.5,

#                'хват двумя руками')

# # classic_sword = Sword('Дежурный', 1.2,

# #                       'хват одной рукой')

# # my_sword = Sword('Дракон',  2.0, 'Хват тремя руками', 'diamond')

# # # Печатаем созданные объекты.

# # print(katana)

# # print(classic_sword)

# # print (my_sword)

# import datetime
# import time

# class Quest:
#     def __init__ (self, name, description, goal):
#         self.name = name
#         self.description = description
#         self.goal = goal
#         self.start_time = None
#         self.end_time = None


#     def accept_quest (self):
#         if self.end_time is not None:
#             return ('С этим приключением вы уже справились')
#         else:
#             self.start_time = datetime.datetime.now()
#             return (f'Начало {self.name} положено')


#     def pass_quest (self):
#         if self.start_time is None:
#             return ('Нельзя завершить то, что не начал выполнять')
#         else:    
#             self.end_time = datetime.datetime.now()
#             completion_time = self.end_time - self.start_time

#             return (f'Квест "{self.name}" окончен. Время выполнения квеста:'
#                     f'{completion_time}')

    
#     def __str__ (self):
#         base_message = f'Цель квеста {self.name}: {self.goal}'
#         message = None
#         if self.start_time is not None and self.end_time == None:
#             message = base_message + 'Квест выполняется'
#             return message
#         elif self.end_time is not None:
#             message = base_message + 'Квест выполнен'
#             return message
#         else:
#             return base_message
    
# quest_name = 'Сбор пиксельники'
# quest_goal = 'Соберите 12 ягод пиксельники.'
# quest_description = '''
# В древнем лесу Кодоборье растёт ягода "пиксельника".
# Она нужна для приготовления целебных снадобий.
# Соберите 12 ягод пиксельники.'''


# new_quest = Quest(quest_name, quest_description, quest_goal) 

# # print(new_quest)
# # print(new_quest.accept_quest())

# # time.sleep(3)

# # print(new_quest.pass_quest())



# print(new_quest.pass_quest())

# print(new_quest)

# print(new_quest.accept_quest())

# print(new_quest)

# time.sleep(3)

# print(new_quest.pass_quest())

# print(new_quest)

# print(new_quest.accept_quest())

def start_training(choice_char_class):
    """
    Принимает на вход имя и класс персонажа.4
    Возвращает сообщения о результатах цикла тренировки персонажа.

    """


    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}

    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        # Замените блок условных операторов на словарь
        # и вынесите его из цикла. Здесь останется одно условие
        # принадлежности введённой команды словарю.
        # В функции print() будет вызываться метод класса,
        # который соответствует введённой команде.
        if cmd == 'attack':
            print(attack.Person)
        if cmd == 'defence':
            print(defence.Person)
        if cmd == 'special':
            print(special.Person)
    return 'Тренировка окончена.'
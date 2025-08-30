from random import randint

Default_Attact = 5
Default_Deffence = 10
Default_Stamina = 80
BRIEF_DESC_CHAR_CLASS = 'Условное описание'

class Person: 
# Методы атаки, защиты и спешал базово задаются здесь, далее - наследуются другими классами

    RANGE_VALUE_ATTACK = (1,3)
    RANGE_VALUE_DEFFENCE = (1,5)
    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15


    def __init__ (self, char_name):
        self.name = char_name
            

    
    def attack(self) -> str:
        value_attack = Default_Attact + randint (*self.RANGE_VALUE_ATTACK)
        return (f'Вы ({self.name}) нанесли {value_attack} единиц урона')
        

    def defence (self) -> str:
        value_deffence = Default_Deffence + randint(*self.RANGE_VALUE_DEFFENCE)
        return (f'Вы ({self.name}) нанесли {value_deffence} единиц урона')

    def special (self) -> str:
        return (f'{self.name} применил умение {self.SPECIAL_SKILL} и получил + {self.SPECIAL_BUFF} урона')
    
    def __str__ (self):
        return (f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}')

class Warrior(Person):

    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = Default_Stamina + 25
    SPECIAL_SKILL = 'Выносливость'
    
    

class Mage(Person):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = Default_Attact + 40
    SPECIAL_SKILL = 'Атака'
    
    

class Healer(Person):
    BRIEF_DESC_CHAR_CLASS = (' Лечит')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = Default_Deffence + 30
    SPECIAL_SKILL = 'Защита' 



def choice_char_class(char_name: str) -> Person:
    """
    Возвращает строку с выбранным
    классом персонажа.
    """
    # Добавили словарь, в котором соотносится ввод пользователя и класс персонажа.
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    
    approve_choice: str  = None
    
    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                           'за которого хочешь играть: Воитель — warrior, '
                           'Маг — mage, Лекарь — healer: ')
        char_class: Person = game_classes[selected_class](char_name)
        # Строка выше - это просто пиздец, я еле-еле понимаю логику кода
        # Вывели в терминал описание персонажа.
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class 


def start_training(char_name, char_class : Person):
    """
    Принимает на вход имя и класс персонажа.4
    Возвращает сообщения о результатах цикла тренировки персонажа.

    """


    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    
    commands = {
        'attack': char_class.attack,
        'defence': char_class.defence,
        'special': char_class.special
    }

    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd in commands:
            result = commands[cmd]()
            print(result)
        elif cmd != 'skip':
            print('Неизвестная команда! Попробуйте: attack, defence, special или skip')
    return 'Тренировка окончена.'
    
def main() -> str:
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class(char_name)
    print(start_training(char_name, char_class))


main()
class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

# Вот тут функции фактически одинаковые, не красиво
    def describe(self, full):
        return (f'Размер птицы: {self.name} - {self.size}')


class Parrot (Bird):
    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color

    def describe(self, full):
        full_message = (f'Попугай {self.name} — заметная птица,'
                        f'окрас её перьев — {self.color},'
                        f'а размер — {self.size}.'
                        'Интересный факт: попугаи чувствуют ритм,'
                        'а вовсе не бездумно двигаются под музыку.'
                        'Если сменить композицию,'
                        'то и темп движений птицы изменится.')
        if full is False:
            return super().describe(full)
        else:
            return full_message
        
    def repeat (self, phrase):
        return (f'Попугай {self.name} говорит: {phrase}')
        


class Penguin (Bird):
    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus

    def describe(self, full):
        full_message = (f'Размер пингвина {self.name}'
                        f'из рода {self.genus} — {self.size}.'
                        ' Интересный факт: однажды группа геологов-разведчиков'
                        ' похитила пингвинье'
                        ' яйцо, и их принялась преследовать вся стая,'
                        ' не пытаясь, впрочем, при этом нападать.'
                        ' Посовещавшись, похитители вернули птицам'
                        ' яйцо,и те отстали.')
        if full is False:
            return super().describe(full)
        else:
            return full_message

    def swimming (self):
        return (f'{self.name} плавает со средней скоростью 11 км/ч')
kesha = Parrot('Apa', 'Средний', 'Красный')
kowalski = Penguin('Королевский', 'Большой', 'Aptenodytes')


print(kesha.describe(False))
print(kowalski.describe(True))

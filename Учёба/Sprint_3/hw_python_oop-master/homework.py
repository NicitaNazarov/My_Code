class InfoMessage:

    def __init__(self, training_type, duration, distance):
        """Информационное сообщение о тренировке.""" 
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        

    def get_message(self):
        return (f'Тип тренировки: {self.training_type:.3f}; Длительность: {self.duration:.3f} ч.;'
                f' Дистанция: {self.distance:.3f} км;'
                f'Ср. скорость: {self.get_mean_speed:.3f} км/ч; Потрачено ккал: {self.calories:.3f}')
    
    # pass

M_IN_KM = 1000 #Нужно для перевода метров в километры

class Training:
    """Базовый класс тренировки."""
    LEN_IN_STEP = 0.65
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.time = duration
        self.weight = weight
        pass

    def get_distance(self) -> float:
        return self.action * self.LEN_STEP/M_IN_KM
        """Получить дистанцию в км."""
        # pass

    def get_mean_speed(self) -> float:
        return self.get_distance / self.time
        """Получить среднюю скорость движения."""
        # pass

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        # pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        # pass


class Running(Training):
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79 
    
    """Тренировка: бег."""

    def get_spent_calories(self) -> float:
        ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed + self.CALORIES_MEAN_SPEED_SHIFT)
        * self.weight / M_IN_KM * (self.time/60))
    # pass


class SportsWalking(Training):
    CALORIES_MEAN_SPEED_MULTIPLIER = 0.035
    CALORIES_MEAN_SPEED_SHIFT = 0.029
    HEIGHT_IND = 10
    
    def __init__(self, action: int, duration: float, weight: float, height) -> None:
        super().__init__(action, duration, weight)
        self.height = height
    
    def get_spent_calories(self) -> float:
        ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.weight + (self.get_mean_speed**2 / self.height/ self.HEIGHT_IND)
         *self.CALORIES_MEAN_SPEED_SHIFT * self.weight) * (self.time/60))
    """Тренировка: спортивная ходьба."""
    # pass


class Swimming(Training):
    LEN_IN_STEP = 1.38
    CALORIES_MEAN_SPEED_MULTIPLIER = 1,1
    CALORIES_MEAN_SPEED_SHIFT = 2

    def __init__(self, action: int, duration: float, weight: float, lenght_pool, count_pool) -> None:
        super().__init__(action, duration, weight)
        self.lenght_pool = lenght_pool
        self.count_pool = count_pool
    
    def get_mean_speed(self) -> float:
        return self.lenght_pool * self.count_pool / M_IN_KM / (self.time/60) 
    
    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed + self.CALORIES_MEAN_SPEED_MULTIPLIER) *
        self.CALORIES_MEAN_SPEED_SHIFT * self.weight * (self.time / 60))
    """Тренировка: плавание."""
    pass


def read_package(training_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)


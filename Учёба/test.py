# # import time

# # numbers = []

# # for num in range (10**6):
# #     numbers.append(num)

# # start_time_2 = time.time()

# # if 999999 in numbers:
# #     print(True)
# # print (time.time() - start_time_2)


# # import time
# # numbers = set()

# # for num in range (10**6):
# #     numbers.add(num)

# # start_time = time.time()

# # if 999999 in numbers:
# #     print ("True")

# # final_time = time.time() - start_time

# # print (final_time)



# # num_string_1 = '100 13 2 143 12 3 55 4 64 18 56'

# # num_string_2 = '234 2 56 432 3 100 12 99 43 18 31 64'

# # overlap = set(num_string_1.split()) & set(num_string_2.split())

# # print(len(overlap))


# # id_string = '32 48 2 6 14 58 2 88 9 14 123 48 3 17 42 42 7'

# # id_string_dub_removed = id_string.split()
# # IDs = []

# # for i in id_string_dub_removed:
# #     if i not in IDs:
# #         IDs.append(i)
# #     else:
# #         print (f'Найдено повторяющееся ID {i}')

# # output = IDs.sort

# # print (output)




# # movie_ratings = [3.7, 5.0, 4.3, 4.0]
# # movies = ['Матрица', 'Хакеры', 'Трон', 'Кибер']

# # list_good = []
# # list_bad = []

# # movies_bad = []
# # movies_good = []

# # for i in range(len(movie_ratings)):
# #     rating = movie_ratings [i]
# #     movie = movies [i]

# #     if rating < 4.0:
# #         list_bad.append(rating)
# #         movies_bad.append(movie)
# #         print(f'Фильм {movie} удалён из поиска, так как его рейтинг слишком низкий: {rating}')
        
# #     else:
# #         list_good.append(rating)
# #         movies_good.append (movie)
# #         print(f'У фильма {movie} хорошие оценки: {rating}' )
    

# # # print (list_good)
# # # print (movies_good)

# # movies_output = dict(zip(movies_good, list_good))

# # print(movies_output)



# # favorite_movies = {}


# # recommended_movies = {
# #     'Хенкок': {'rating': 4.5, 'review': 'Смотреть можно'},
# #     'Матрица': {'rating': 4.7, 'review': 'Фильм крут'},
# #     'Кибер': {'rating': 2.5, 'review': 'Так себе киношечка'},
# #     'Трон': {'rating': 3.8, 'review': 'Так себе киношечка'},
# #     'Мстители': {'rating': 4.7, 'review': 'Фильм крут'},
# #     'Хакеры':  {'rating': 4.5, 'review': 'Смотреть можно'}
# # }


# # for movie, discription in recommended_movies.copy().items():
# #     review = discription.get('review')
# #     rating = discription.get('rating')
# #     if discription.get('rating') < 4:
# #         print (f'Фильм не рекомендуется к просмотру {movie} {review} {rating}')
# #         del movie
# #     else:
# #         favorite_movies[movie] = discription
# #         print (f'Фильм рекомендован к просмотру {movie} {review} {rating}')

# # print (favorite_movies)
# # print ('II')


# # a = 1
# # 2
# # b = '2'

# # c = ['Анатолий', 3.15, '3 поросёнка']


# # result = f'Суммой чисел {a}, {int(b)} и {int(c[1] - 0.15)} будет 6'
# # print(result)


# # # # Эта функция складывает значение первой переменной и второй, при этом второй переменной может быть список (т.к * запихивает значения в переменную)
# # # def rating_fun (coef, *ratings):
# # #     for rating in ratings:
# # #         print (coef + rating)

# # # x = 1
# # # rating_fun (x, 1, 2, 3, 4, 5, 6, 7, 8)

# # # n = int(input())
# # # students = {}
# # # for _ in range(n):
# # #     line = input().split()
# # #     name = line[0]  
# # #     marks = list(map(float, line[1:]))
# # #     students[name] = marks

# # # student_name = input()

# # # marks = [1,2,3,4,5,6,7,8,9,10]
# # # for mark in marks:
# # #     summ = sum(marks)
# # #     output = summ / len(marks)

# # # print(f'{output:.2f}')   


# # # !!!! Модуль DATETIME !!!!

# # import datetime as DT

# # print (DT.datetime.now())





# # a = int(input('Введите первое число'))
# # b = int(input('Введите второе число'))

# # if a > b:
# #     print (f'Значение {a} > {b}')

# # elif a == b:
# #     print (f'{a} = {b}')

# # else:
# #     print (f'{a} < {b}')


# # massive = [8,11]
# # massive.sort()
# # print (massive [0])


# import datetime as DT

# a = input ('Введите имя')
# b = input ('Введите дату вашего рождения')

# birthdays = []
# for i in birthdays:
#     birthdays.append[a]
#     birthdays.append[b]
# print (birthdays)

# # lera_birthday = DT.date (2015, 5, 16)
# # maxim_birthday = DT.date (2011, 12, 16)
# # today = DT.date.today()

# # print(lera_birthday)
# # print(maxim_birthday)
# # print(today)

# # today_year = today.year

# # def get_days_to_birthday (name, birth_date):
# #     if today > birth_date.replace (year = today_year):

# #         days_to_birthday = today - birth_date.replace (year = today.year)
        
# #     else:
# #         days_to_birthday = today - birth_date.replace (year = today.year-1)
        
    
# #     print (f'{name}, до твоего дня рождения осталось : {days_to_birthday.days} дня')
    
# # for birthday in birthdays:
# #     name, birth_date = birthday
# #     birth_date = DT.datetime.strptime(birth_date, '%d.%m.%Y').date()
# #     get_days_to_birthday(name, birth_date)


import datetime as DT


WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = dict({(100, '9:22:12'),
              (200, '9:23:12'),
              (300, '9:24:12')}  # Словарь для хранения полученных данных.


def check_correct_data(data):

    for item in data:

        if len(data) != 2 or data == None:
            print ('False')
            return False
        
        else:
            print('True')
            return True
        
    # Если длина пакета отлична от 2

    # или один из элементов пакета имеет пустое значение -

    # функция вернет False, иначе - True.

for i in storage_data.items():
    steps, time = i
    check_correct_data (storage_data)
    time = DT.datetime.strptime(f'{time}', '%H:%M:%S').time()
    
    
print (storage_data)



def check_correct_time(time):

    """Проверка корректности параметра времени."""

    # Если словарь для хранения не пустой

    # и значение времени, полученное в аргументе,

    # меньше или равно самому большому значению ключа в словаре,

    # функция вернет False.

    # Иначе - True 




def get_step_day(steps):

    """Получить количество пройденных шагов за этот день."""

    # Посчитайте все шаги, записанные в словарь storage_data,

    # прибавьте к ним значение из последнего пакета

    # и верните  эту сумму.

def get_distance(steps):

    """Получить дистанцию пройденного пути в км."""

    # Посчитайте дистанцию в километрах,

    # исходя из количества шагов и длины шага.
def get_spent_calories(dist, current_time):
    """Получить значения потраченных калорий."""
    # В уроке «Последовательности» вы написали формулу расчета калорий.
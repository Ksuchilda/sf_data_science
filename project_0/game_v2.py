"""Игра угадай число
Компьютер сам загадывает и сам угадывает"""

import numpy as np

def fast_predict(number:int=1) -> int:
    """Угадываем число делением интервала пополам

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # задаем начальные значения: счетчик попыток и интервал чисел угадывания
    count = 0
    interval = [1, 100]
    
    # запускаем бесконечный цикл поиска загаданного числа
    
    while True:
        
        count += 1 # увеличиваем счетчик попыток
        predict_number = (interval[0] + interval[1]) // 2 # предполагаемое число - середина интервала
        
        if number == predict_number:
            # выход из цикла, если угадали
            break 
        
        # если предполагаемое число число меньше загаданного-меняем правую границу интервала на это число
        elif number < predict_number:
            interval = [1, predict_number] 
            
        # если больше, то меняем левую границу           
        else:
            interval = [predict_number, 100]
            
    return count

def score_game(fast_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        fast_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    # угадываем каждое число и формируем список из количества попыток
    for number in random_array:
        count_ls.append(fast_predict())

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    
    return score

# RUN
if __name__ == '__main__':
    score_game(fast_predict)
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
    
    # задаем начальные значения: счетчик попыток, минимальную и максимальную границу интервала чисел угадывания
    count = 0
    min_num = 1
    max_num = 100
    predict_number = (min_num + max_num)//2
    
    # запускаем бесконечный цикл поиска загаданного числа пока загаданное число не равно предполагаемому
    
    while number != predict_number:
        
        count += 1 # увеличиваем счетчик попыток
        
        # если загаданное число больше предполагаемого-меняем минимальную границу на предполагаемое число
        # предполагаемое число ищем по формуле с новым интервалом
        if number > predict_number:
            min_num = predict_number + 1
            predict_number = (min_num + max_num)//2
            
        # если загаданное число меньше предполагаемого-меняем максимальную границу на предполагаемое число
        # предполагаемое число ищем по формуле с новым интервалом   
        elif number < predict_number:
            max_num = predict_number - 1
            predict_number = (min_num + max_num)//2
        
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
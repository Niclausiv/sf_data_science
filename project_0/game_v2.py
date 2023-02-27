"""Библиотека  game_v2.py содержит в себе две документированные 
функции: random_predict() и score_game()
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """ Функция принимает загаданное число и возвращает число попыток
    Просто угадываем на random, никак не используя информацию
    больше загаданное число или меньше.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count



def score_game(random_predict) -> int:
    """ Функция для оценки
    Эта функция необходима, чтобы определить, за какое число попыток программа
    угадывает наше число.
    За какое количество попыток в среднем за 1000 подходов угадывает 
    наш  алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Количество попыток, за которое алгоритм в среднем угадывает число:{score}")
    #return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)

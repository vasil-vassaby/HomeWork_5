# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

import random

print('----Игра с конфетами----')


def get_candy():
    """Создание случайного количества конфет"""
    number = random.randint(30, 100)
    return number


def get_player(player_count):
    """
    Формирование списка имен игроков
    Параметр: player_count - количество игроков
    """
    players = []
    for i in range(player_count):
        player_name = input(f'Введите имя игрока {i + 1}: ')
        players.append(player_name)
    return players





number_candies = get_candy()
print('Количество конфет в начале игры: ' + str(number_candies))
number_of_players = get_player(2)
winner = find_winner(number_of_players, number_candies)
print(f'Победитель {winner}')
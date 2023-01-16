# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

import random


def get_candy():
    """Создание и вывод случайного количества конфет"""
    print('----Игра с конфетами----')
    number = random.randint(30, 100)
    print('Количество конфет в начале игры: ' + str(number))


def get_player(player_count):
    """Определение игроков"""
    players = []
    for i in range(player_count):
        player_name = input(f'Введите имя игрока {i + 1}: ')
        players.append(player_name)
    return players


def find_winner(players):
    """Определение и вывод победителя"""
    is_winner = False
    winner_name = None
    while not is_winner:
        for player in players:
            print(f'Ход игрока ' + player.title())
            player_number = int(input('Введите количество конфет: '))
            if player_number <= 28:
                number = number - player_number
                if number == 0:
                    is_winner = True
                    winner_name = player
                    break
                print('Остаток конфет: ' + str(number))
            else:
                print('Введите количество конфет не более чем 28!')
    else:
        print(f'Победитель {winner_name.title()}')


get_candy()
number_of_players = get_player(2)
find_winner(number_of_players)


from random import randint as ri


def description():
    """ Формирование заголовка для игры """
    print('----Игра с конфетами----')


def get_candy():
    """ Формирование случайным образом общего количества конфет от 30 до 150 шт """
    return ri(30, 150)


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


def print_candy(count: int):
    """ Вывод в консоль информации по количеству конфет в начале игры """
    print('Количество конфет в начале игры: ' + str(count))


def print_win(win: str):
    """ Вывод в консоль информации о победителе игры """
    print(f'Победитель {win}')

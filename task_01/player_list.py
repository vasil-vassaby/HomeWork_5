
from random import randint as ri

players = []
total = None


def description():
    """ Формирование заголовка для игры """
    print('--------ИГРА С КОНФЕТАМИ--------')


def get_candy():
    """ Формирование случайным образом общего количества конфет от 30 до 150 шт """
    global total
    total = ri(30, 150)
    print('Количество конфет в начале игры: ', total)


def get_player():
    """ Формирование списка имен игроков """
    global players
    for i in range(2):
        player_name = input(f'Введите имя игрока {i + 1}: ')
        players.append(player_name)
    return players


def find_winner():
    """ Определение и вывод победителя """
    global total
    global players
    is_winner = False
    while not is_winner:
        for player in players:
            active = True
            while active:
                print('Ход игрока ', player.title())
                player_number = int(input('Введите количество конфет: '))
                if player_number <= 28:
                    active = False
                    total -= player_number
                    if total == 0:
                        is_winner = True
                        winner_name = player
                        print(f'Победитель {winner_name.title()}')
                else:
                    print('Конфет должно быть не более чем 28!')
            print('Остаток конфет: ', total)

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# а) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint as ri
import winner as win
import player_list as pl

print('----Игра с конфетами----')


def get_candy(): return ri(30, 100)


number_candies = get_candy()
print('Количество конфет в начале игры: ' + str(number_candies))
number_of_players = pl.get_player(2)
winner = win.find_winner(number_of_players, number_candies)
print(f'Победитель {winner}')

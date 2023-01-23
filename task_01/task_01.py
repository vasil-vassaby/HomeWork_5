# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# а) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'


import winner as win
import player_list as pl


def start_game():
    pl.description()
    number_candies = pl.get_candy()
    pl.print_candy(number_candies)
    number_of_players = pl.get_player(2)  # два игрока
    winner = win.find_winner(number_of_players, number_candies)
    pl.print_win(winner)

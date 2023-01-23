
import winner as win
import player_list as pl


def start_game():
    pl.description()
    number_candies = pl.get_candy()
    pl.print_candy(number_candies)
    number_of_players = pl.get_player(2)  # два игрока
    winner = win.find_winner(number_of_players, number_candies)
    pl.print_win(winner)

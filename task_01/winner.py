def find_winner(players, count_candies):
    """
    Определение и вывод победителя
    Параметры: players - список имен игроков, count_candies - количество конфет
    """
    is_winner = False
    while not is_winner:
        for player in players:
            active = True
            while active:
                print(f'Ход игрока ' + player.title())
                player_number = int(input('Введите количество конфет: '))
                if player_number <= 28:
                    active = False
                    count_candies -= player_number
                    if count_candies == 0:
                        winner_name = player
                        return winner_name.title()
                else:
                    print('Конфет должно быть не более чем 28!')
            print('Остаток конфет: ' + str(count_candies))

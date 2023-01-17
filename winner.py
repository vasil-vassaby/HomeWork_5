def find_winner(players, count_candies):
    """
    Определение и вывод победителя
    Параметры: players - список имен игроков, count_candies - количество конфет
    """
    is_winner = False
    winner_name = None
    while not is_winner:
        for player in players:
            active = False
            while not active:
                print(f'Ход игрока ' + player.title())
                player_number = int(input('Введите количество конфет: '))
                if player_number <= 28:
                    active = True
                    count_candies = count_candies - player_number
                    if count_candies == 0:
                        is_winner = True
                        winner_name = player
                        break
                    break
                else:
                    print('Конфет должно быть не более чем 28!')
            print('Остаток конфет: ' + str(count_candies))
    else:
        return winner_name.title()
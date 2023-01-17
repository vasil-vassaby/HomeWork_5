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
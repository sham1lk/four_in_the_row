from game import Game, Player

PLAYER_NUMBER = 2
WEIGHT = 7
HEIGHT = 6

NUM_TO_STR = {
    1: 'first',
    2: 'second'
}


def get_players():
    identifiers = ['.']
    for i in range(PLAYER_NUMBER):
        print('Please enter name of the {} player'.format(NUM_TO_STR[i + 1]))
        name = input()
        print(
            'Please enter identifier of the {} player(one '
            'character to be shown in the board)'.format(
                NUM_TO_STR[i + 1]))
        identifier = input()
        while len(identifier) > 1 or identifier in identifiers:
            print(
                'identifier should be character and should be unique,'
                ' try again')
            identifier = input()
        identifiers.append(identifier)
        player = Player(name, identifier)
        players.append(player)


if __name__ == '__main__':
    players = []
    print("Hello! Let's get to know each other first!")
    get_players()
    game = Game(players, HEIGHT, WEIGHT)
    game.start_game()

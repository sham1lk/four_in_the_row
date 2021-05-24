class Game:
    def __init__(self, players, height, weight):
        self.players = players
        self.height = height
        self.weight = weight
        self.winner = None
        self.board = self.create_board()
        self.current_move = 0
        self.players_num = len(players)
        self.num_to_win = 4

    def start_game(self):
        while not self.winner:
            print('Turn: {}'.format(
                self.players[self.current_move % self.players_num].name))
            self.print_board()
            move = self.make_move()
            self.winner = self.check_winner(*move)
            self.current_move += 1
        print("Player {} won".format(
            self.players[(self.current_move - 1) % self.players_num].name))

    def check_winner(self, row, column):
        ident = self.players[self.current_move % self.players_num].identifier

        def check_down():
            k = 0
            for i in range(row, self.height + 1):
                if self.board[i][column] != ident:
                    return k
                k += 1
            return k

        def check_hor():
            k = 0
            for i in range(column, self.weight):
                if self.board[row][i] != ident:
                    break
                k += 1
            for i in range(column):
                if self.board[row][i] != ident:
                    break
                k += 1
            return k

        def check_ver():
            k = 0
            l = 0
            for i in range(min(self.height - row, self.weight - column)):
                if self.board[row + i][column + i] != ident:
                    break
                k += 1
            for i in range(min(row - 1, column - 1)):
                if self.board[row - 1 - i][column - 1 - i] != ident:
                    break
                k += 1
            for i in range(min(row - 1, self.weight - 1 - column)):
                if self.board[row - 1 - i][column - 1 + i] != ident:
                    break
                l += 1
            for i in range(min(self.height - row, column)):
                if self.board[row + i][column - i] != ident:
                    break
                l += 1

            return max(k, l)

        return (check_ver() >= self.num_to_win or
                check_hor() >= self.num_to_win or
                check_down() >= self.num_to_win)

    def make_move(self):
        print('Insert column number:')
        number = input()
        while not number.isdigit() or int(number) < 1 or int(
                number) > self.weight:
            print('number should be in range [1, {}]'.format(self.weight))
            number = input()
        number = int(number)
        for i, row in reversed(list(enumerate(self.board))):
            if row[number - 1] == 0:
                self.board[i][number - 1] = self.players[
                    self.current_move % self.players_num].identifier
                return (i, number - 1)

        print("Column already full, try again")
        self.make_move()

    def print_board(self):
        for i in range(self.height + 1):
            for j in range(self.weight):
                print(self.board[i][j], end=' ')
            print('')

    def create_board(self):
        board = [
            [0 for i in range(self.weight)] for j in range(self.height)
        ]
        numbers = [[i + 1 for i in range(self.weight)]]
        return numbers + board


class Player:
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

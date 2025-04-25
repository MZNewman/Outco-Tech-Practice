
class TicTacToe:
    def __init__(self):
        self.board = Board(3)
        self.player = "X"
        self.rounds = 9

    def play(self):
        valid_moves = ["0","1","2"]
        while self.rounds > 0:
            print("------")
            self.print_current_players_turn()
            valid = False
            while not valid:
                confirmed = False
                while not confirmed:
                    print("This is the current board state:")
                    self.board.print_board()
                    row = input("Please give the row number from 0 to 2 where you want to make your move: ")
                    col = input("Please give the col number from 0 to 2 where you want to make your move: ")
                    yes = input("Please type \"yes\" to confirm that this is the move you want, otherwise type something else: ")
                    if yes == "yes" and row in valid_moves and col in valid_moves:
                        confirmed = True
                    else:
                        print("Try again please")
                row = int(row)
                col = int(col)
                if self.board.can_place_piece(row, col):
                    valid = True
                    self.print_current_move(row, col)
                else:
                    self.print_invalid_move(row, col)
            self.play_round(row, col)
            if self.board.check_win_condition(self.player):
                self.declare_winner(self.player)
                return
            else:
                self.switch_player()
                self.decrement_rounds()
        if self.board.check_win_condition(self.player):
            self.declare_winner(self.player)
            return
        else:
            self.declare_tie()
            return

    def play_round(self, row, col):
        self.board.place_piece(row, col, self.player)

    def print_current_players_turn(self):
        print("It is " + self.player + "\'s turn")

    def decrement_rounds(self):
        self.rounds -= 1

    def declare_winner(self, player):
        print("Player " + self.player + " wins!")
        self.board.print_board()

    def declare_tie(self):
        print("Game over! This game is a tie")
        self.board.print_board()

    def print_current_move(self, row, col):
        print("An " + self.player + " is being placed at row " + str(row) + " and column " + str(col))

    def print_invalid_move(self, row, col):
        print("The move you have chosen is invalid, please try again")

    def switch_player(self):
        if self.player == "X":
            self.player = "0"
        else:
            self.player = "X"



class Board:
    def __init__(self, dim):
        self.board = [['E' for x in range(dim)] for y in range(dim)]

    def print_board(self):
        for row in self.board:
            print(row)

    def can_place_piece(self, row, col):
        if self.board[row][col] == 'E':
            return True
        return False

    def place_piece(self, row, col, player):
        self.board[row][col] = player

    def check_win_condition(self, player):
        if self.check_diagonals(player):
            return True
        if self.check_rows(player):
            return True
        if self.check_columns(player):
            return True
        return False

    def check_diagonals(self, player):
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        return False

    def check_rows(self, player):
        if self.board[0][0] == player and self.board[0][1] == player and self.board[0][2] == player:
            return True
        if self.board[1][0] == player and self.board[1][1] == player and self.board[1][2] == player:
            return True
        if self.board[2][0] == player and self.board[2][1] == player and self.board[2][2] == player:
            return True
        return False

    def check_columns(self, player):
        if self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player:
            return True
        if self.board[0][1] == player and self.board[1][1] == player and self.board[2][1] == player:
            return True
        if self.board[0][2] == player and self.board[1][2] == player and self.board[2][2] == player:
            return True
        return False


# Uncomment to test
ttt = TicTacToe()
ttt.play()
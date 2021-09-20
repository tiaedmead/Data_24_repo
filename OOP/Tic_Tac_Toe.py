

class Board:
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",]

    def display(self):
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("-----------")
        print(" %s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6]))
        print("-----------")
        print(" %s | %s | %s " % (self.cells[7], self.cells[8], self.cells[9]))

    def update_cell(self, cell_num, player):
        if self.cells[cell_num] == " ":
            self.cells[cell_num] = player

    def is_winer(self, player):
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True


board = Board()


print("Welcome to tic-tac-toe")


def refresh_game():
    board.display()
    print("\n")


while True:
    refresh_game()

    x_move = int(input("Player X.  Please choose from 1-9 >>> "))
    print("\n")
    board.update_cell(x_move, "X")

    refresh_game()

    if board.is_winer("X"):
        print("X WINS!")
        play_again = input("Would you like to play again? (Y/N) >>> ").upper()
        if play_again == "Y":
            continue
        else:
            break

    o_move = int(input("Player O.  Please choose from 1-9 >>> "))
    board.update_cell(o_move, "O")
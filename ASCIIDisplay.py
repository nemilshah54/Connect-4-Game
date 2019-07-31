class ASCIIDisplay:
    def __init__(self,spacing = 1):
        self.spacing = spacing

    def printState(self, b):
        plus = '+'
        minus = '-'
        line = '|'
        index = 0;

        for i in range(0, b.rows + 1):

            if i == b.rows:  # Last line of the board.
                for i in range(0, b.cols + 1):
                    if i ==  b.cols:
                        print(plus)
                    else:
                        print(plus, end="")
                        for i in range(0, ( self.spacing * 2) + 1):
                            print(minus, end="")

                for x in range(0,  b.cols):
                    for i in range(0, self.spacing + 1):
                        print(" ", end="")
                    print(x + 1, end="")
                    for i in range(0, self.spacing):
                        print(" ", end="")
            else:  # All lines except last of the board.

                for j in range(0,  b.cols + 1):  # +-+-
                    if j ==  b.cols:
                        print(plus)
                    else:
                        print(plus, end="")
                        for k in range(0, (self.spacing * 2) + 1):
                            print(minus, end="")

                for j in range(0,  b.cols + 1):  # | | | |
                    if j == 0:
                        print(plus, end="")
                        for k in range(0, self.spacing):
                            print(" ", end="")
                        print( b.cells[i][j].piece.disp, end="")
                        for k in range(0, self.spacing):
                            print(" ", end="")
                    elif j ==  b.cols:
                        print(line)
                    else:
                        print(line, end="")
                        for k in range(0, self.spacing):
                            print(" ", end="")
                        print(b.cells[i][j].piece.disp, end="")
                        for k in range(0, self.spacing):
                            print(" ", end="")

        print("\n\n")

        # print("\n")

    @staticmethod
    def displayInstructions():
        print("Type the column in which you wish to move.")

    @staticmethod
    def boardSpacing ():
        print("Please choose the board spacing: ",end = "")

    @staticmethod
    def prompt_for_move(turn_count, player_name, player_symbol):
        print("Turn {}: {} ({}), choose your move: ".format(turn_count, player_name, player_symbol), end='')

    @staticmethod
    def invalid_move_outsideBoard():
        print("Invalid move, outside board, try again:", )

    @staticmethod
    def invalid_move_coloumn_full( number):
        print("Invalid move, coloumn " + str(number) + " is full, try again:")

    @staticmethod
    def matchTie():
        print("\n\nMatch is Tie.  Play again? (y/n): ")

    @staticmethod
    def win( name):
        print("\n\n" + name + " Wins! Play again? (y/n): ")

    @staticmethod
    def endGame():
        print("Goodbye !")

    @staticmethod
    def newlines():
        print("\n\n")


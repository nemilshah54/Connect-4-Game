from Board import Board
from Player import Player
from Piece import Connect_four
from KeyboardConsoleInput import KeyboardConsoleInput


class Connect_four_Runner:
    def __init__(self, display):
        self.displayDriver = display  # Display object.
        self.displayDriver.boardSpacing ()
        space =KeyboardConsoleInput.read_spacing()
        self.displayDriver.displayInstructions()
        self.displayDriver.spacing = space
        self.board = Board( 6, 7)     # Creating the board of 6*7.
        self.displayDriver.printState ( self.board)

        self.listofPlayers = []
        p1 = Player(1, 'R', "Player 1")
        self.listofPlayers.append (p1)
        p2 = Player(1, 'B', "Player 2")
        self.listofPlayers.append(p2)


    def reinitialize(self, display):


        self.board = Board(6, 7)  # Creating the board of 6*7.
        self.displayDriver.printState(self.board)
        self.listofPlayers = []
        p1 = Player(1, 'R', "Player 1")
        self.listofPlayers.append(p1)
        p2 = Player(1, 'B', "Player 2")
        self.listofPlayers.append(p2)


    def play_game(self):
        playagain = " "
        playagain2 = " "

        turn = 1  # Count the no. of moves.
        exitGame = 0  # Flag to exit from both the loop.s
        while 1:
            for iter in self.listofPlayers:

                # Allowing each player to choose a move.
                selectMove = iter.chooseMove(turn)

                # Making a move and updating the board. Terminates the loops if player is won.
                while (self.board.makeMove(selectMove, iter.pieceMarker, iter) == False):
                    selectMove = iter.chooseMove(turn)

                # Displaying Board for the next player.
                self.displayDriver.printState(self.board)
                #self.displayBoard(self.boardpieces, self.space)
                turn = turn + 1

                # Check for Tie.
                countForTie = 0
                for i in range(0, self.board.rows):
                    for j in range(0, self.board.cols):
                        if self.board.cells[i][j].piece.disp != ' ':
                            countForTie = countForTie + 1

                boardLength = self.board.rows * self.board.cols
                if countForTie == boardLength:
                    self.displayDriver.matchTie()
                    playagain =  KeyboardConsoleInput.read_playagain()
                if playagain == "n":
                    exitGame = 1
                    break
                if playagain == "y":
                    self.reinitialize( self.displayDriver)
                    for iter in self.listofPlayers:
                        iter.winStatus = False
                        turn = 1
                        playagain = " "
                        continue

                # If player is won, terminate both the loop, and play the match again.
                if iter.winStatus == True:
                    self.displayDriver.win(iter.playerName)
                    playagain2 =  KeyboardConsoleInput.read_playagain()
                if playagain2 == "n":
                    exitGame = 1
                    break
                if playagain2 == "y":
                    self.reinitialize( self.displayDriver)
                    for iter in self.listofPlayers:
                        iter.winStatus = False
                        turn = 1
                        playagain2 = " "
                        continue

            if (exitGame):
                break

        self.displayDriver.endGame()

    def check_if_winner(self, p):
        return False

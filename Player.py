from  KeyboardConsoleInput import KeyboardConsoleInput
from ASCIIDisplay import ASCIIDisplay

class Player:
    def __init__(self, player_number=-1, piece_marker="?", player_name="Unknown"):
        self.playerNumber = player_number
        self.pieceMarker = piece_marker
        self.playerName = player_name
        self.winStatus = False

    def chooseMove(self, turn):

        ASCIIDisplay.prompt_for_move ( turn,  self.playerName, self.pieceMarker)
        selectMove = KeyboardConsoleInput.read_move()
        ASCIIDisplay.newlines()

        return selectMove

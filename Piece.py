import abc

class Piece(abc.ABC):
    def __init__(self, col=-1, row=-1, b=None):
        self.col = col
        self.row = row
        self.disp = ' '
        self.board = b


    def debug_string(self):
        if(debug_flag):
            return self._printInfo()
        return ""

    def _printInfo(self):
        s = "col: " + str(self.col) + "\nrow: " + str(self.row) + "\ntype of piece: " + self.disp
        print(s)
        return s

    def __str__(self):
        return self.disp


class Connect_four(Piece):
    def __init__(self, player, col=-1, row=-1):
        super().__init__(col, row)

    def set_location(self, loc):
        pass

    def validate_move(self, x, y):
        pass

    def make_move(self, x, y):
        pass

    def _printInfo(self): # Unnecessary as of now
        super()._printInfo()
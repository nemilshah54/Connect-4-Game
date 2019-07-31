from Cell import Cell
from Piece import Piece
from ASCIIDisplay import ASCIIDisplay


class Board:
    '''A container for the collection of spaces in the playing field'''
    def __init__(self, row =6, col =7):

        '''Connect 4 board 6*7

        cells is a 2 dimensional list of cell objects
        The first list is the list of columns
        Each column contains a list of rows'''
        self.rows = row
        self.cols = col
        self.cells = []

        for cell_row in range(self.rows):
            new_row = []
            for cell_col in range(self.cols):
                new_row.append(Cell( cell_row, cell_col))
            self.cells.append(new_row)

    def makeMove(self,number, playerPiece, player):
        if number < 1 or number > self.cols:
            ASCIIDisplay.invalid_move_outsideBoard()
            return False

        for i in range(0, self.rows):

            if self.cells[i][number - 1].piece.disp == " " and i == self.rows - 1:  # Bottom of the board.
                self.cells[i][number - 1].piece.disp = playerPiece
                # pop the piece from playerpieces.

                # check winner function.
                self.checkWinner(i, number - 1, playerPiece, player)

                return True  # valid move.

            if (self.cells[i][number - 1].piece.disp == "R" or self.cells[i][number - 1].piece.disp == "B") and i == 0:  # Top of the board.
                ASCIIDisplay.invalid_move_coloumn_full(number)
                return False  # Invalid move.

            if self.cells[i][number - 1].piece.disp == "R" or self.cells[i][number - 1].piece.disp == "B":  # Midde of board.
                self.cells[i - 1][number - 1].piece.disp = playerPiece

                # check winner function.
                self.checkWinner(i - 1, number - 1, playerPiece, player)
                return True  # valid move.

    def add_piece(self, row, col, p):
        return self.cells[row][col].update(p)

    def move_piece(self, origCol, origRow, col, row, p):
        pass





    def checkWinner(self, i, j, playerpiece, player):

        if (self.checkHorizontal(i, j, playerpiece)):
            player.winStatus = True

        if (self.checkVertical(i, j, playerpiece)):
            player.winStatus = True

        if (self.checkDiagonal(i, j, playerpiece)):
            player.winStatus = True

    def checkHorizontal(self, i, j, playerPiece):
        # 1  Horizontal left 3.
        if (j >= 3):
            if self.cells[i][j - 1].piece.disp == playerPiece and self.cells[i][j - 2].piece.disp == playerPiece and self.cells[i][j - 3].piece.disp == playerPiece:
                return True

        # 2  Horizontal right 3.
        if (self.cols - 1 - j >= 3):
            if self.cells[i][j + 1].piece.disp == playerPiece and self.cells[i][j + 2].piece.disp == playerPiece and self.cells[i][j + 3].piece.disp == playerPiece:
                return True

        # 3  Horizontal left 1 right 2
        if (j > 0 and self.cols - 1 - j >= 2):
            if self.cells[i][j - 1].piece.disp == playerPiece and self.cells[i][j + 1].piece.disp == playerPiece and self.cells[i][j + 2].piece.disp == playerPiece:
                return True
        # 4  Horizontal left 2 right 1
        if (j >= 2 and self.cols - 1 - j >= 1):
            if self.cells[i][j - 1].piece.disp == playerPiece and self.cells[i][j - 2].piece.disp == playerPiece and self.cells[i][j + 1].piece.disp == playerPiece:
                return True

        return False

    def checkVertical(self, i, j, playerPiece):
        # 1 Vertical down 3.
        if (self.rows - 1 - i >= 3):
            if self.cells[i + 1][j].piece.disp == playerPiece and self.cells[i + 2][j].piece.disp == playerPiece and  self.cells[i + 3][j].piece.disp == playerPiece:
                return True
        return False

    def checkDiagonal(self, i, j, playerPiece):
        # 1  Diagonal up 3.   done.
        if (i >= 3 and self.cols - 1 - j >= 3):
            if self.cells[i - 1][j + 1].piece.disp == playerPiece and self.cells[i - 2][j + 2].piece.disp == playerPiece and  self.cells[i - 3][j + 3].piece.disp == playerPiece:
                return True  # Checked for First Quadrant of Graph in 2d matrix (Upper Right)

        if (j >= 3 and i >= 3):
            if self.cells[i - 1][j - 1].piece.disp == playerPiece and self.cells[i - 2][j - 2].piece.disp == playerPiece and self.cells[i - 3][j - 3].piece.disp == playerPiece:
                return True  # Checked for Second Quadrant of Graph in 2d matrix (Upper Left)

        # 2  Diagonal down 3.   done.
        if (self.rows - 1 - i >= 3 and j >= 3):
            if self.cells[i + 1][j - 1].piece.disp == playerPiece and self.cells[i + 2][j - 2].piece.disp == playerPiece and  self.cells[i + 3][j - 3].piece.disp == playerPiece:
                return True  # Checked for Third Quadrant of Graph in 2d matrix (Lower left)

        if (self.cols - 1 - j >= 3 and self.rows - 1 - i >= 3):
            if self.cells[i + 1][j + 1].piece.disp == playerPiece and self.cells[i + 2][j + 2].piece.disp == playerPiece and self.cells[i + 3][j + 3].piece.disp == playerPiece:
                return True  # Checked for Fourth Quadrant of Graph in 2d matrix (Lower right)

        # 3  Diagonal down 1 and up 2   done
        if (i >= 2 and self.cols - 1 - j >= 2 and self.rows - 1 - i >= 1 and j >= 1):
            if self.cells[i + 1][j - 1].piece.disp == playerPiece and self.cells[i - 1][j + 1].piece.disp == playerPiece and self.cells[i - 2][j + 2].piece.disp == playerPiece:
                return True  # Checked for 1 and 3 Quadrant of Graph in 2d matrix (Upper Right and lower left)

        if (self.cols - 1 - j >= 1 and self.rows - 1 - i >= 1 and i >= 2 and j >= 2):
            if self.cells[i + 1][j + 1].piece.disp == playerPiece and self.cells[i - 1][j - 1].piece.disp == playerPiece and  self.cells[i - 2][j - 2].piece.disp == playerPiece:
                return True  # Checked for 2 and 4 Quadrant of Graph in 2d matrix (Upper Left and lower right)

        # 4  Diagonal down 2 and up 1  done
        if (i >= 1 and self.cols - 1 - j >= 1 and self.rows - 1 - i >= 2 and j >= 2):
            if self.cells[i + 1][j - 1].piece.disp == playerPiece and self.cells[i + 2][j - 2].piece.disp == playerPiece and self.cells[i - 1][j + 1].piece.disp == playerPiece:
                return True  # Checked for 1 and 3 Quadrant of Graph in 2d matrix (Upper Right and lower left)

        if (i >= 1 and j >= 1 and self.cols - 1 - j >= 2 and self.rows - 1 - i >= 2):
            if self.cells[i + 1][j + 1].piece.disp == playerPiece and self.cells[i + 2][j + 2].piece.disp == playerPiece and  self.cells[i - 1][j - 1].piece.disp == playerPiece:
                return True  # Checked for 2 and 4 Quadrant of Graph in 2d matrix (Upper Left and lower right)

        return False









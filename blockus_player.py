import numpy as np

from blockus_piece import Piece
class Player:

    def __init__(self, color):
        self.color = color
        self.pieces = self.init_pieces()
        


    def init_pieces(self):
        piece_1 = Piece(np.array([[1]]), self.color)
        piece_2 = Piece(np.array([[1, 1]]), self.color)
        piece_3A = Piece(np.array([[1, 1],
                             [0, 1]]), self.color)
        piece_3B = Piece(np.array([[1, 1, 1]]), self.color)

        piece_4A = Piece(np.array([[1, 1, 1, 1]]), self.color)
        piece_4B = Piece(np.array([[1, 1, 1],[0, 0, 1]]), self.color)

        #Finish this later

        return([piece_1, piece_2, piece_3A, piece_3B, piece_4A, piece_4B])


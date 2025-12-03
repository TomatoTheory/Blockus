import numpy as np

class Piece:
    def __init__(self, orientation, color):
        """Orientation is an np array that stores the shape of the block. Pieces can be rotated"""
        self.lt = orientation
        self.color = color
    
    def rotate(self):
        self.lt = np.array(np.rot90(self.lt))
        return self.lt


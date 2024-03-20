from enum import Enum

'''
    Does placing edges pieces first make a difference
'''

class Piece:
    def __init__(self, left, top, bottom, right): # NOTE: is corner can be determined from other fields
        self.left = left
        self.top = top
        self.bottom = bottom
        self.right = right

class EdgeType(Enum):
    FLAT = 1
    IN = 2
    OUT = 3

class Side(Enum):
    def __init__(self, type, piece):
        self.type = type
        self.piece = piece

class Puzzle:
    def __init__(self, pieces, rows, cols):
        self.remaining_pieces = pieces
        self.solution = [[None] * cols] * rows
    
    def solve(self, pieces):
        
        for row in range(self.rows):
            for col in range(self.cols):


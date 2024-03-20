'''
Implement a jigsaw puzzle. Design the data structures and explain an algorithm to solve the puzzle.
In jigsaw puzzles we take the piece, and make a meaningfull things from the set of pieces given to us.

SOLUTION NOTE: 
    Keep track of exposed edges essentially edges that are exposed and can still be fit w. another piece?
    Have Edge keep track of parent piece?

    Solution starts by filling out all edges (perimeter of puzzle) and keeping a list of exposed edges

    Solution increases time performance by:
        iterating over all pieces
        adding each edge to one of three arrays (inner, outer, edge) so when checking if a piece fits you only need to
        check from possible candiddates
        Note that this where having an edge link out to its piece helps
        How does this work with rotating of pieces? If orientation isnt and issue this works
'''

from enum import Enum
from typing import List, Type


class Puzzle:
    def __init__(self, pieces, row, col): # TODO: Figure out how to annotat custome type
        self.pieces = pieces
        self.solution = [[None] * col] * row
    def add_piece(self, piece, row, col):
        pass
    def does_fit(self, piece, row, col) -> bool:
        pass
    def solve(self):
        '''
            Q: Are the pieces in the correct orientation as they should be in final result
            Q: Is puzzle square same number of pieces length-wise and width-wise
            Consider using backtracking to create every possible permutattion of puzzle. 
            If possible fits insert move on to next
            If you reach a point where no piece fits backtrack
            But this will return possible answers? rather than a single solution
            This would require setting up a board (NxN) and giving each piece an id to allocate to board
            Q: Will answers be unique? Are there ways to blindly construct a puzzel w.o all pieces in the right order?

            NOTE: Need a fxn to determin if a piece fits

            IDEA:
                Use backtracking
                helper function for recursive calls
                start at 0,0
                move row by row
                at each cell check if each piece fits. rotate up to 4 times. note that edge and corner pieces will
                have a special way of being handled.
                if no piece fits remove prev piece otherwise add to board and move on to next col
                when you reach final col you call function with next row
                once you are at the final col of the final row. add solution to solution array
        '''

        pass
    def solve_row(self, row: int) -> None:
        pass

class Piece:
    def __init__(self, left, top, bottom, right): # NOTE: is corner can be determined from other fields
        self.left = left
        self.top = top
        self.bottom = bottom
        self.right = right
        # NOTE: Python Syntax: https://stackoverflow.com/questions/38125328/what-does-a-backslash-by-itself-mean-in-python
        # Q: Should I be concerned about linter call out
        self.is_corner = (self.left == EdgeType.FLAT and self.top == EdgeType.FLAT) \
            or (self.top == EdgeType.FLAT and self.right == EdgeType.FLAT)  \
            or (self.right == EdgeType.FLAT and self.bottom == EdgeType.FLAT)  \
            or (self.bottom == EdgeType.FLAT and self.left == EdgeType.FLAT) 


    '''
            T
            ^
        L <- ->R
            B
    '''
    def rotate_90_clockwise(self):
        self.left, self.top, self.right, self.bottom = self.bottom, self.left, self.top, self.right
        '''
            alt would need to loop keeping a temp for one that was overriden. Or maybe there isn't a way to do this TODO:
        '''

class Edge:
    def __init__(self, type, piece):
        self.type = type
        self.piece = piece

class EdgeType(Enum):
    FLAT = 1
    IN = 2
    OUT = 3


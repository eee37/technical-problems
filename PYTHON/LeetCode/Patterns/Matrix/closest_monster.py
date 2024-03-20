'''
#closest_monster

Imagine we are building an AI to play a computer game in which a player moves around a two-dimensional grid filled with stationary monsters. 

Monsters look very scary, and if a player looks vertically or horizontally and sees a monster, they become scared.

Write a function that takes a board, and returns the following information:
 - Player's location, such as the row and column indexes
 - Number of spaces between the player and the closest scary monster they can see vertically or horizontally.

Board constraints:
 - The board is a two-dimensional grid of characters
 - An empty space on the board is represented by a dash '-'
 - The player is denoted by the letter 'P'
 - Monsters are denoted by the letter 'M'

Example board:
board1 = [
  ['-', '-', '-', 'M', '-', '-'],
  ['-', '-', '-', '-', 'M', '-'],
  ['-', 'M', '-', 'P', '-', '-'],
  ['M', '-', '-', '-', '-', '-'],
  ['-', 'M', '-', '-', '-', '-'],
]
Expected Output (in any format): 
(2,3), 1

You may return the player's location in whatever form you'd like. A standard approach that you are welcome to use is to define the top-left corner of the board as (0,0), and give coordinates in (row,column) order.

Complexity Analysis variables:
r = number of rows
c = number of columns
'''


from typing import List


def player_position(board: List[List[str]]):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'P':
                return (row, col)
    return -1

def nearest_monster_distance(board: List[List[str]]):
    row, col = player_position(board)
    
    # for distance in range(max(row + 1, col + 1, len(board) - row, len(board[0]) - col   ))
    for distance in range(max(len(board), len(board[0]))):
        if row - distance >= 0:
            # print(f'{distance} {board[row - distance][col]}')
            if board[row - distance][col] == 'M':
                return ((row, col), distance-1)
        if row + distance < len(board):
            if board[row + distance][col] == 'M':
                return ((row, col), distance-1)
        if col - distance >= 0:
            if board[row][col - distance] == 'M':
                return ((row, col), distance-1)
        if col + distance < len(board[0]):
            if board[row][col + distance] == 'M': 
                return ((row, col), distance-1)
    return ((row, col), -1)
        
board1 = [
  ['-', '-', '-', 'M', '-', '-'],
  ['-', '-', '-', '-', 'M', '-'],
  ['-', 'M', '-', 'P', '-', '-'],
  ['M', '-', '-', '-', '-', '-'],
  ['-', 'M', '-', '-', '-', '-'],
]
print(nearest_monster_distance(board1))
# returns (2,3), 1

board2 = [
  ['P', '-', '-', '-', '-', '-'],
  ['-', '-', 'M', '-', 'M', '-'],
  ['-', '-', '-', '-', '-', '-'],
  ['M', '-', '-', 'M', '-', '-'],
  ['-', 'M', '-', '-', '-', '-'],
]
# returns (0,0), 2
print(nearest_monster_distance(board2))

board3 = [
  ['M', 'M', 'M'],
  ['-', '-', 'P'],
]
# returns (1,2), 0
print(nearest_monster_distance(board3))
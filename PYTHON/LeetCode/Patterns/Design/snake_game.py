'''
******************* PROBLEM STATEMENT
LC # 353

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY:
SPACE COMPLEXITY:

******** SOLUTION

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* TAGS
'''

'''
    Idea is to keep track of snake' head prev {length} position + prev tail position using a list (stack + queue)
        keeping track of tail's prev postion allows us to update snake after it eats food and expands
        pos = position of head
        hist = position of body with prev position of tail at position 0
    Question
        - is it possible to food to start at 0,0?
TODO: Return to
NOTE: Took way too long!
We do not need to keep track of prev tail position instead when a snake consumes food not remove prev tail from occipied space
Solution uses 
    1. queue for tracking snake
    2. set for tracking cells occupied by snake
    3. does not use matrix
    4. given solution is much cleaner. follows DRY and logic flows clearer
'''
from typing import List


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        # assign class vars
        self.w = width
        self.h = height
        self.food = food
        # -- create board
        self.board = [[''] * width] * height # Note: Py Syntax Multiplier is outside of arr brackets
        self.pos = [0,0] # Note: Py Syntax Tuple values cannot be re-assinged
        self.hist = deque() # hist must be of size of snakenote in case snake grows
        self.length = 1
        self.score = 0
        
        # set board to start state
        if food:
            f = food.pop(0)
            print(self.board)
            self.board[f[0]][f[1]] = 'food'
        self.board[0][0] = 'snake'
            
    def update_food(self) -> None: # NOTE: Py Syntax recall class methods take in self unless they are static
        if self.board[self.pos[0]][self.pos[1]] == 'food':
            self.length += 1 # Remember to update tail
            self.score +=1
            if self.food:
                f = self.food.pop(0)
                self.board[f[0]][f[1]] = 'food'
    
    def update_snake(self, old_pos: List[int]) -> bool:
        # update tail and head
        self.hist.appendleft(old_pos)
        if len(self.hist) == self.length + 1:
            to_remove = self.hist.pop()
            self.board[to_remove[0]][to_remove[1]] = ''
        if old_pos[0] == 0 and old_pos[1] == 0:
            self.board[0][0] = ''
        # see if snake collided
        r, c = self.pos
        
        print(f'board:{self.board}, pos:{self.pos}, old pos:{old_pos}')
        if self.board[r][c] == 'snake':
            return -1
        self.board[r][c] = 'snake'
        return self.score
        
        

    def move(self, direction: str) -> int:
        old_pos = self.pos
        if direction == 'U':
            self.pos[0] = self.pos[0] - 1
            if self.pos[0] < 0:
                return -1
            self.update_food()
            return self.update_snake(old_pos)
                
        
        elif direction == 'R':
            self.pos[1] = self.pos[1] + 1
            if self.pos[1] >= self.w:
                return -1
            self.update_food()
            return self.update_snake(old_pos)
            
        elif direction == 'L':
            self.pos[1] = self.pos[1] - 1
            if self.pos[1] < 0:
                return -1
            self.update_food()
            return self.update_snake(old_pos)
        
        elif direction == 'D':
            self.pos[0] = self.pos[0] + 1
            if self.pos[0] >= self.h:
                return -1
            self.update_food()
            return self.update_snake(old_pos)
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
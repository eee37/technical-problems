'''
******************* PROBLEM STATEMENT
LC # 52

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY:
SPACE COMPLEXITY:

******** SOLUTION

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* TAGS
#Backtracking #Recursion
'''

'''
    https://leetcode.com/problems/n-queens-ii/solution/
    NOTES:
    General
        BigO hard to grasp
    From LC Solutions
        Solution has good readability
        Instead of using a 2-dimensional array to track the board uses 4 sets to represent rows, cols, diags and antidiag that are taken. This reduces space complexity to O(n) from O(n**2)
        This also reduces n**2 factor in time complexity
        Note that to remove just update sets after path explored
        Note sets solutions to 0 as default to prevent increment solutions when non-exist in path explored
'''
# TODO: Go over enum
'''
0  1  2   3
1 1,1 1,2 1,3
2 2,1 2,2 2,3
3 3,1 3,2 3,3
'''
from typing import List

# TODO: Go over enum
'''
0  1  2   3
1 1,1 1,2 1,3
2 2,1 2,2 2,3
3 3,1 3,2 3,3
'''
class Solution:
    def totalNQueens(self, n: int) -> int:
        # False means not in strike distance
        state = [False] * n
        state = [state] * n # NOTE: Syntax note the paranthesis
        
        return self.check_row(0,state, 0)
        
        
    
    
    def check_row(self, row: int, state: List[List[bool]], count: int) -> int: # DO WE NEED COL?
        n = len(state)
        for col in range(0, n):
            # not in striking distance
            if not state[row][col]:
                print('1')
                if row == n-1:
                    print('2') # NEVER GETTING HERE
                    count += 1
                else:
                    self.update_state(row, col, True, state) # TODO:
                    count = self.check_row(row + 1, state, count)
                self.update_state(row, col, False, state)
        return count

    
    
    def update_state(self, row: int, col: int, is_add: bool, state: List[List[bool]]) -> None: # NOTE: Python Syntax don't forget self in methods
        # ways to attack: by row, col, diag, anti-diag
        
        # # col
        # for c in range(0, len(state)):
        #     state[row][c] = is_add
        # # row
        # for r in range(0, len(state)):
        #     state[r][col] = is_add
        
        # diag
        diag = row - col
        
        # anti-diaf
        anti = row + col
        
        for r in range(0, len(state)):
            for c in range(0, len(state)):
                # col
                if c == col or r == row or r + c == anti or r - c == diag:
                    state[c][r] = is_add
        
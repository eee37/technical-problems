'''
NOTE:
    https://leetcode.com/problems/search-a-2d-matrix-ii/solution/
    Approach 3: 
        * Actually uses div conq approach similar to bin search
        * Cleverly exploits matrix conditions
        * Recursively
            * Search middle column until you find either target or an element larger than target
            * You can then eliminate top-left quandrant from consideration as they will be less than target (NOTE: you scanned that column and items in those rows and that quadrant will be smaller)
            * You can then also eliminate bottom-right quadrant from from consideration as they will be larget than target (NOTE: going further right, down guarantees you will only find larget numbers)
        * Interesting for analyzing Big O!! 
    Approach 4:
        * More performant
        * Start bottom left corner
        * Move right if current tile is too small. move up if its too large. when you are out of bounds is not found
        * Exploits property of matrix. 
            * bc you are moving towards bottom-right
            * if too small moving right eliminates part of matrix that must be smaller (NOTE: You were on bottom right corner of matrix - largest contained value)
            * if too large moving bottom eliminates part of matrix that must be smaller (NOTE: You were on top left corner of matrix - smallest contained value)
#DivideConquer #Recursion
    soln1: 
        TIME: O(2**(m*n)) 
        SPACE: O(1)
    soln2: 
        TIME: O(m*n) 
        SPACE: O(m*n)
'''
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search_neigh(r, c, len_r, len_c, target, matrix, memo): # Do you need to pass target, matrix
            if matrix[r][c] == target:
                return True
            
            if memo[(r,c)] is not None:
                return memo[(r, c)]
            
            found_c = False
            found_r = False
            
            if r < len_r - 1:
                found_r = search_neigh(r + 1, c, len_r, len_c, target, matrix, memo)
                
            if c < len_c - 1:
                found_c = search_neigh(r, c + 1, len_r, len_c, target, matrix, memo)
                
            
            memo.update({(r,c): found_r or found_c})
            return memo[(r,c)]
            
            
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        memo = defaultdict(lambda : None)
        
        return search_neigh(0, 0, len(matrix), len(matrix[0]), target, matrix, memo)

# Approach # 1
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search_neigh(r, c, len_r, len_c, target, matrix): # Do you need to pass target, matrix
            if matrix[r][c] == target:
                return True
            
            found_c = False
            found_r = False
            
            if r < len_r - 1:
                found_r = search_neigh(r + 1, c, len_r, len_c, target, matrix)
                
            if c < len_c - 1:
                found_c = search_neigh(r, c + 1, len_r, len_c, target, matrix)
            
            return found_r or found_c
            
            
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        return search_neigh(0, 0, len(matrix), len(matrix[0]), target, matrix)
'''
    
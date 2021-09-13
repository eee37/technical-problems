'''
******************* PROBLEM STATEMENT

******************* NOTES

TIME COMPLEXITY: O(logMN)
SPACE COMPLEXITY: O(1)

******************* SOLUTION
'''

from typing import List


class Solution:
    '''
        matrix: r x c
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        num_rows = len(matrix)
        num_cols = len(matrix[0])

        start = 0
        end = num_rows * num_cols - 1

        while end >= start: # NOTE: >= needed
            mid = start + (end - start) // 2

            r = mid // num_cols
            c = mid % num_cols

            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                start = mid + 1
            else:
                end = mid - 1

        return False

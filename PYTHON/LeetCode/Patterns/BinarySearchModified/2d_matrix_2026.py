import math
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        left = 0
        row_len = len(matrix[0])
        right = len(matrix) * len(matrix[0]) - 1 # NOTE: Zero index so largest would be at index nm -1

        while left <= right:
            mid = left + (right - left) // 2

            row = math.floor(mid/row_len)
            col = (mid % row_len)
            if matrix[row][col] == target:
                return True
            elif target < matrix[row][col]:
                right = mid - 1
            else:
                left = mid + 1
        
        return False


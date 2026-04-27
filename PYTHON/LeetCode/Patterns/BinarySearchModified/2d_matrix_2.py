class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix[0]) == 0:
            return False
        r = 0
        c = len(matrix[0]) - 1

        while r <= len(matrix) - 1 and c >= 0:
            if matrix[r][c] == target:
                return True
            elif target < matrix[r][c]:
                c -= 1
            else:
                r += 1
        
        return False

        
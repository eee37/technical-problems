'''
NOTE:
Problem #3
https://leetcode.com/problems/set-matrix-zeroes/

'''
from collections import defaultdict

def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return matrix
    


    # find which rows and columns have 0s. NOTE: This violates space complexity. Saying that needs to be modified in place implies O(1) space complexity
    zero_rows = [] # SPACE COMPLEXITY = O(M+N)
    zero_cols = []

    # O(n) -> m*n
    for row_i, row in enumerate(matrix):
        for col_i, cell in enumerate(row):
            if cell == 0:
                zero_rows.append(row_i)
                zero_cols.append(col_i)
    
    # O(n) -> m*n
    if zero_rows:
        for row_i in zero_rows:
            row = matrix[row_i]
            for col_i, _ in enumerate(row):
                matrix[row_i][col_i] = 0
    
    # O(n) -> m*n
    if zero_cols:
        for row_i, _ in enumerate(matrix):
            for col_i in zero_cols:
                matrix[row_i][col_i] = 0
    
    return matrix




print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]));
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]));



# def setZeroes(matrix):
#     """
#     :type matrix: List[List[int]]
#     :rtype: None Do not return anything, modify matrix in-place instead.
#     """
#     if len(matrix) == 0 or len(matrix[0]) == 0:
#         return matrix
    
#     num_col = len(matrix[0])

#     # find which rows and columns have 0s
#     zero_indexes = defaultdict(list)

#     # O(n) -> m*n
#     for row_i, row in enumerate(matrix):
#         zero_indexes[row_i] = []
#         for col_i, cell in enumerate(row):
#             if cell == 0:
#                 zero_indexes[row_i].append(col_i)

    
#     for row_i, columns in  zero_indexes.items(): # NOTE: How to iterate key value pairs in map
#         matrix[row_i] = [0] * num_col
    
#     return matrix




print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]));
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]));



class Solution(object):
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements. NOTE: Skip over first row and col bc they are guides to what to set to 0
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well. NOTE: Now we can overwrite the first row
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well. NOTE: We used a bool for first col bc they over lap. [i,0], [0,j] is the same for the first row/col4/9
        if is_col:
            for i in range(R):
                matrix[i][0] = 0
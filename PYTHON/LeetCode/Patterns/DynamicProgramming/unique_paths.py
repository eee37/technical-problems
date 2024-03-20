'''
    Note: One a border cell is reached only 1 possible route to the target cell exists
    Approach one considers an mxn matrix where each cell contains the number of paths to that cell. Note that all 'boundary' cells must be initiated with 1 as there is only one route to them.
    Also note that for inner cell rxc the number of routes to it are the sum of routes to r-1xc and rxc-1
'''


# This solution is not fast enough
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = 0
        if m + n <= 1:
            return count
        return self.count(1, 1, m, n)

    def count(self, r: int, c: int, m: int, n: int) -> int:
        if r == m or c == n:
            return 1
        if r != m and c != n:
            return self.count(r + 1, c, m, n) + self.count(r, c + 1, m, n)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1] * n] * m  # init matrix
        # count paths by row
        for r in range(1, m):
            for c in range(1, n):
                matrix[r][c] = matrix[r - 1][c] + matrix[r][c - 1]
        return matrix[m - 1][n - 1]

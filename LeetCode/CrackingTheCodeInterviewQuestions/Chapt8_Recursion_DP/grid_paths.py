from typing import List # NOTE: List type needs to be import from typing
'''
    O(x,y) = 2^{x+y}
    NOTE: Really bad time complexity. Best possible runtime is O(n+y) since at least will need to visit each cell once
    This runtime can be achieved by:
    1: https://leetcode.com/problems/unique-paths-ii/: Using the matrix to keep tabs on the number of ways that cell is reachable 
    and using that iteratively to get the value for remaining cells. Trick is to calculate value for 1st row and 1st col first
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        y_limit = len(obstacleGrid)
        x_limit = len(obstacleGrid[0])

        if y_limit <= 0 or x_limit <= 0:
            return 0

        if obstacleGrid[0][0] == 1 or obstacleGrid[y_limit - 1][x_limit -1] == 1: # NOTE: Cant have an obstacle in start or end
            return 0

        return Solution.num_paths(0, 0, obstacleGrid, x_limit - 1, y_limit - 1)

    @staticmethod
    def num_paths(x, y, og, x_limit, y_limit):

        # reached bottom-right corner
        if x == x_limit and y == y_limit: # NOTE: bottom right cant containe obstacle to be reachable
            return 1

        d, r = 0, 0

        # can move down
        if y + 1 <= y_limit:
            if og[y + 1][x] == 0:
                d = Solution.num_paths(x, y + 1, og, x_limit, y_limit)

        # can move right
        if x + 1 <= x_limit:
            if og[y][x + 1] == 0:
                r = Solution.num_paths(x + 1, y, og, x_limit, y_limit)

        return d + r

if __name__ == '__main__':
    sol = Solution()
    print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
    print(sol.uniquePathsWithObstacles([[0,1],[0,0]]))
    print(sol.uniquePathsWithObstacles([[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],[1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],[0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],[1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],[0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],[1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]]))
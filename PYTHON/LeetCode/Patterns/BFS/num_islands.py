'''
    LC: # 200
'''
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        count = 0
        for r, r_arr in enumerate(grid):
            for c, c_arr in enumerate(grid[r]):
                if grid[r][c] == "1":
                    count += 1
                    self.bfs(grid, r, c)
        return count

    def bfs(self, grid: List[List[str]], r: str, c: str) -> int:
        queue = [[r,c]]
        grid[r][c] = "0" # NOTE: Needed to prevent counting an island more than once
        while queue:
            nxt = queue.pop(0)
            r = nxt[0]
            c = nxt[1]
            if r - 1 >= 0:
                if grid[r - 1][c] == "1":
                    queue.append([r - 1, c])
                    grid[r - 1][c] = "0" # NOTE: Needs to be done when added to queue to prevent same coordinate from being added multiple times
            if r + 1 <= len(grid) - 1: # NOTE: Remember 0-based index requires - 1
                if grid[r + 1][c] == "1":
                    queue.append([r + 1, c])
                    grid[r + 1][c] = "0" # NOTE: Needs to be done when added to queue to prevent same coordinate from being added multiple times
            if c - 1 >= 0:
                if grid[r][c - 1] == "1":
                    queue.append([r, c - 1])
                    grid[r][c - 1] = "0" # NOTE: Needs to be done when added to queue to prevent same coordinate from being added multiple times
            if c + 1 <= len(grid[0]) - 1:
                if grid[r][c + 1] == "1":
                    queue.append([r, c + 1])
                    grid[r][c + 1] = "0" # NOTE: Needs to be done when added to queue to prevent same coordinate from being added multiple times
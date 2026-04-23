"""
    TIME: O(m*n)
    SPACE: O(m*n)
    
    Approach #1 uses a delimeter entry (-1, -1) to detect new levels
    They also use directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] to loop through possible next moves

    Approach #2 Uses in place algo to bring space to O(1) but traverses entire grid at each round
"""

from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rc = len(grid)
        if not grid[0]:
            return -1
        cc = len(grid[0])

        fresh = 0
        queue = deque([])
        
        for ri, row in enumerate(grid):
            for ci, cell in enumerate(row):
                if cell == 1:
                    fresh += 1
                elif cell == 2:
                    queue.append((ri, ci))
        print("grid", grid)
        print("queue", queue)
        print("fresh", fresh)
        print("---------------------")
        

        level = 0
        
        while queue:
            converted_in_this_round = False
            print("queue", queue)
            current_length = len(queue)
            print("fresh", fresh)
            for _ in range(current_length):
                print("index", _)
                r,c = queue.popleft()
                if level > 0 and grid[r][c] == 2: # NOTE: cell could have already been processed after first round
                    continue
                else:
                    converted_in_this_round = True
                if level > 0:
                    grid[r][c] = 2
                    fresh -= 1
                if r - 1 >= 0 and grid[r-1][c] == 1:
                    queue.append((r-1,c))
                if r + 1 <= rc - 1 and grid[r+1][c] == 1: 
                    queue.append((r+1,c))
                if c - 1 >= 0 and grid[r][c-1] == 1:
                    queue.append((r,c-1))
                if c + 1 <= cc - 1 and grid[r][c+1] == 1:
                    queue.append((r,c+1))
            if converted_in_this_round: 
                level += 1 # NOTE: Need to have seen at least one rotten in this round to add a level

        print("---------------------")
        print("fresh", fresh)

        if fresh == 0:
            return max(level - 1, 0) # NOTE: We count after each round even when all are rotten so need to subtract one
        else:
            return -1
        


        
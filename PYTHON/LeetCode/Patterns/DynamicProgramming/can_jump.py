'''
Time: O(N**2)
Space: O(N)
'''
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) > 0:
            return self.jump(0, nums)
        return False

    def jumpRec(self, pos: int, nums: List[int]) -> bool:
        if pos == len(nums) - 1:
            return True
        for jump in range(nums[pos]):
            new_pos = pos + jump + 1
            if new_pos <= len(nums) - 1:
                if self.jumpRec(new_pos, nums):
                    return True
        return False

'''
Time: O(N) Didn't understand initially why its O(N^2). Doesn't the memoization table mean we never check an index twice? Apperantly not. but bc we still need to check even if its False its O(N^2). Think of the case where the target is not reachable and each jump is as high as the max jump
NOTE: Need an unknown category
Space: O(N)
One quick optimization we can do for the code above is to check the nextPosition from largest to smallest.
Since the goal is to get to end this is faster
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = ["Unknown"] * len(nums)
        if len(nums) > 0:
            return self.jumpRec(0, nums, visited)
        return False

    def jumpRec(self, pos: int, nums: List[int], visited: List[int]) -> bool:
        if pos == len(nums) - 1:
            return True
        if visited[pos] == "Bad" : # Known not to reach target
            return False
        for jump in range(min(nums[pos], len(nums) - 1 - pos)): # NOTE: 1. Can limit jump to max jump 2. Can start w/ largest jump
            new_pos = pos + jump + 1
            if new_pos <= len(nums) - 1 and visited[pos] != "Bad":
                if self.jumpRec(new_pos, nums, visited):
                    return True
        visited[pos] = "Bad"
        return False

'''
CONCEPT: Trick in optimal solution is to use "Bottom-Up" approach and notice how to determine where index/spot is good w/o iterating
'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        next_true = len(nums) -1
        for index in reversed(range(len(nums))):
            if nums[index] + index >= next_true:
                next_true = index
        return next_true == 0

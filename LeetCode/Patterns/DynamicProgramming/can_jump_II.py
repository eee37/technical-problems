'''
    Lesson: Don't anchor on previous solution
    Idea: Scan arrays keeping track of
        1. Num Jumps
        2. Current Jump End (needed to update other vars)
        3. Farthest Jump (needed to update current jump end)
    The idea is keep track of furthest you can jump and the minimal number of jumps required to take you there. Need to keep track of current jump ending index and index of next jump ending index
    When you get to last index return solution. It's kind of like a moving interval that is updated when certain conditions are met
'''
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        jump_end = 0
        far = 0
        for index in range(len(nums)):
            far = max(far, index + nums[index])
            if index == jump_end and index != len(nums)-1:
                jumps += 1
                jump_end = far
        return jumps
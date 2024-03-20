'''
******************* PROBLEM STATEMENT
153. Find Minimum in Rotated Sorted Array


******************* NOTES

NOTE: // => integer division

TIME COMPLEXITY: O(logN)
SPACE COMPLEXITY: 1

******************* SOLUTION
'''
import math
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        while len(nums) > 1:
            mid = math.floor(len(nums)/2)

            if nums[mid-1]  > nums[mid]:
                return nums[mid]

            if nums[0] < nums[len(nums)-1]:
                nums = nums[:mid]
            else:
                if nums[mid] > nums[0]:
                    nums = nums[mid+1:]
                else:
                    nums = nums[:mid]
        return nums[0]
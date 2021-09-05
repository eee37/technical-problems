# ******************* PROBLEM STATEMENT

# ******************* NOTES

# ******************* SOLUTION
from typing import List


class Solution:
    @staticmethod
    def sortedSquares(nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        squares_index = len(nums) - 1 # could instead use values of left and right to calculate this
        squares = [0] * len(nums) # is it possible to create sorted squares in-place?

        while left <= right: # or while squares_index > 0
            if nums[left]**2 > nums[right]**2:
                squares[squares_index] = nums[left]**2
                left += 1
            else:
                squares[squares_index] = nums[right] ** 2
                right -= 1
            squares_index -= 1

        return squares


if __name__ == '__main__':
    assert Solution.sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
    assert Solution.sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]



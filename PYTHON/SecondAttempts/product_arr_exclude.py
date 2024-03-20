'''
******************* PROBLEM STATEMENT
LC # ___

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY:
SPACE COMPLEXITY:

******** SOLUTION

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* TAGS
'''

from typing import List

# IDEA:
# Use ans as left array. Compute right array as calculating ans

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        for index in range(1, len(nums)):
            ans[index] = ans[index-1] * nums[index-1]
        
        right_product = 1

        for index in range(len(nums)-1, -1, -1):
            ans[index] = right_product * ans[index]
            right_product = right_product * nums[index]

        return ans
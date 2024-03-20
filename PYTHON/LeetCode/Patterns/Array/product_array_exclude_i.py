'''
******************* PROBLEM STATEMENT
LC # 238

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY:
SPACE COMPLEXITY:

******** SOLUTION

TIME COMPLEXITY: 
SPACE COMPLEXITY:

******************* TAGS
'''

'''
    one way to reverse array
    for i in reversed(range(length - 1)):
    NOTE: 
    * I believe it is more efficient to create array of fixed size
    than to create and empty array and append at each iteration
    * Could have reversed right array to make code simpler
    * Code in Solution is much cleaner
    * Most optimal solution reduces space to "O(1)" not counting result array by
    using result as left array and calculating right array on the fly
    *  After noticing catch problem is straightforward
'''
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n

        for i in range(n):
            if i == 0:
                continue
            left[i] = nums[i-1] * left[i-1]

        for j in range(n):
            if j == 0:
                continue
            right[j] = nums[n-j] * right[j-1]

        ans = [0] * n

        for index in range(n):
            right_index = n - 1 - index

            right_product = right[right_index] if right_index > 0 else 1
            left_product = left[index] if index > 0 else 1
            ans[index] = left_product * right_product

        return ans
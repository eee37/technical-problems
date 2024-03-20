'''
    LC #152
    NOTES:
        This solution doesnt work because event number of (-) produce a positive result. Would want to test out every interval of nums where number of negative numbers is even. Would also need to handle 0

        Trick to solution is seeing how capturing min value so far solves the issues ties with odd number of negative values plus handles zeros

        Trick is hard to understand. Need to see how max_pro and min_pro each reset when a max or min chain is broken
        Look at each scenario and see what happens when a num of a new sign appears

        https://leetcode.com/problems/maximum-product-subarray/solution/
'''
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]

        max_pro = nums[0]
        min_pro = nums[0]
        result = max_pro

        for num in nums[1:]:
            old_min = min_pro
            # Update min
            min_pro = min(num, min_pro * num, max_pro * num)
            # Update curr
            max_pro = max(num, max_pro * num, old_min * num) # NOTE: Max so far should be used here not curr

            result = max(max_pro, result)

        return result


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        max_pro = nums[0]
        curr_pro = nums[0]
        curr_sign = self.sign(curr_pro)

        for index, num in enumerate(nums[1:]):
            # reset when
                # curr + and next num - or 0
                # curr - and next num +
            #if (curr_sign == 1 and (self.sign(num) == -1  or self.sign(num) == 0)) or curr_sign == -1 and self.sign(num) == 1:
                #pass
            if curr_pro * num > curr_pro:
                curr_pro = curr_pro * num
                max_pro = max(max_pro, curr_pro)
            else:
                curr_pro = num # one times any nums is the number itself
                max_pro = max(max_pro, curr_pro) # answer wants largest number if products are smaller
                # TODO: Go to where prodcut becomes positive again
        return max_pro

    def sign(self, num: int) -> int:
        if num == 0:
            return 0
        elif num < 0:
            return -1
        else:
            return 1
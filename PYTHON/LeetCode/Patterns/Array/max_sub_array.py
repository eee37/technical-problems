'''
    LC # 53
    NOTES:
        Solution takes advantage of the fact that you dont need to track of interval/indexes just sum
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]


        for num in nums[1:]:
            # we want to reset sum/range when sum of prev nums in interval is negative. the line below achieves that
            curr_sum = max(num, num + curr_sum)
            max_sum = max(curr_sum, max_sum)

        return max_sum
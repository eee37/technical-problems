"""
    Solution # 1: Time O(n) Space O(1)
"""

# class NumArray(object):

#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.nums = nums
        

#     def sumRange(self, left, right):
#         """
#         :type left: int
#         :type right: int
#         :rtype: int
#         """
#         index = left
#         ans = 0
#         while index <= right:
#             ans += self.nums[index]
#             index+=1
#         return ans


"""
    Solution # 1: Time O(1) Space O(n)
"""

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.prefix_sum = [0] * (len(nums) + 1)
        for index in range(1, len(nums)+1):
            self.prefix_sum[index] = self.prefix_sum[index-1] + self.nums[index-1]

        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix_sum[right+1] - self.prefix_sum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


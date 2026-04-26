"""
    The scenario where this type of problem breaks down is  122222222223
    2222231222222.
    ^.     ^  
    If pivot element is 2 and left most is 2 then saying its sorted would be incorrect

    The prime difficulty in this problem would be identify edge case where previous solution no longer holds
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left)// 2

            if nums[mid] == target:
                return True
            elif nums[mid] == nums[left]:
                left = left + 1
            elif nums[left] < nums[mid]: # left partition is sorted
                if nums[left] <= target <= nums[mid]: # in left partition
                    right = mid - 1
                else:
                    left = mid + 1
            else: # right parition is sorted
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return False

        
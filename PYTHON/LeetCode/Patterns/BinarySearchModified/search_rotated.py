from typing import List


'''
******************* PROBLEM STATEMENT

******************* NOTES
    PART II. 
        1. Determine which subarray you are in 
        2. Determine which direction to search given known subarray location
TIME COMPLEXITY: O(logN)
SPACE COMPLEXITY: O(1)

******************* SOLUTION


'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        start = 0
        end = len(nums) -1

        while end >= start:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            # in second sub array
            if nums[mid] < nums[start]:
                if target < nums[mid] or target > nums[end]:
                    end = mid - 1
                else:
                    start = mid + 1
            # in first sub array
            else:
                if target > nums[mid] or target < nums[start]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

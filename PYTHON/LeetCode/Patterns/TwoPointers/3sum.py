# ******************* PROBLEM STATEMENT
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
# ******************* NOTES
# IDEAS:
# worst time complexity is N**3
# 1. HashMap: {SUM: LIST<TUPLE<INT, INT>>} -> N**2
# 2. Idea is there a way to combine mergesort or quicksort w/ creating hashmap and reduce complexity to NlogN

# ******************* SOLUTION
# For some reason it returns duplicates. Moving on
from typing import List


class Solution:
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        # NOTE: Base Case
        if len(nums) < 3:
            return []

        nums.sort()
        ans = []
        for index, num in enumerate(nums):
            if num > 0:
                break
            if index > 0: # NOTE: Prevents duplicates
                if nums[index-1] == nums[index]:
                    break
            # ans.append([twoSumList + [num] for twoSumList in Solution.twoSum(nums, -num)]) # This seems to add an empty list when Solution.twoSum returns empty list
            twoSumSols = Solution.twoSum(nums, -num)
            for twoSumSol in twoSumSols:
                ans.append(twoSumSol + [num])
        return ans

    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        ans = []

        while left < right: # LAST TIME BEFORE LEFT AND RIGHT POINT TO SAME ELEMENT
            if nums[left] + nums[right] == target:
                ans.append([nums[left], nums[right]])
                left += 1
                right -= 1 # IS THIS NECESSARY SHOULDN'T Left increment and while loop below sufffice
                while left <= right and nums[left] == nums[left-1]:
                    left += 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        print(ans, target)
        return ans

    # Answer to https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
    @staticmethod
    def twoSumIndex(nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        ans = []

        while left <= right:
            if nums[left] + nums[right] == target:
                ans.append([left + 1, right + 1])
                left += 1 # NOTE: This alone should prevent duplicate pair od indeces from being returned
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        print(ans)
        return ans[0]

if __name__ == '__main__':
    print(Solution.threeSum([-1,0,1]))
    assert Solution.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]



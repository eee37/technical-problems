'''
    Leetcode Link: https://leetcode.com/problems/contains-duplicate/
    Difficulty: EASY
    Attemp: 1
    Notes:
        1. Can be implemented in less lines using set: https://www.programiz.com/python-programming/methods/built-in/set

'''
from typing import List


class Solution:
    @staticmethod
    def containsDuplicate(nums: List[int]) -> bool:
        seen = dict()

        for value in nums:
            if seen.get(value):
                return True
            seen.update({value: True})

        return False


if __name__ == "__main__":
    print(Solution.containsDuplicate([1,2,3,1]))
    print(Solution.containsDuplicate([1,2,3,4]))
    print(Solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
    print(Solution.containsDuplicate([]))
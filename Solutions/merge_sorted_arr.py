'''
******************* PROBLEM STATEMENT
LC # 88

******************* NOTES
Struggled to write a clean solution in time

NOTE: 
    Clean solution starts from the end of both filled parts of the array and fills nums1 from back to front
    REMEMBER if there is a simple solution to go over it before moving to more optimal solution

******** MY IMPLEMENTATION:

TIME COMPLEXITY: O(m+n)
SPACE COMPLEXITY: O(1)

******** SOLUTION

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* TAGS
'''

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        IDEA: 
        1. 'Flip' nums1 so that empty spots are allocated to first n slots
        2. Use 2 pointer method to fill nums1. 
            Use a special marker to denote empty slots in nums1
        
        """
        # In this case we dont want to do anything even shift
        if n == 0:
            return
        
        # Shift nums1 n places
        for index in range(m-1, -1, -1):
            nums1[index + n] = nums1[index]
            nums1[index] = float('inf')
        
        pointer1 = n # NOTE: Pointer 1 starts at n since nums 1 was shifted n units to the right
        pointer2 = 0

        index = 0
        
        print(nums1)
        
        while index < m+n and pointer2 < n: # NOTE: Wont be able to compare when pointer1 = m+n as it will be out of bounds. We can stop when nums2 is finished being processed
            print(f'nums1 {pointer1} nums2 {pointer2} {nums1}')
            if pointer2 == n or (pointer1<m+n and pointer2 <n and nums1[pointer1] <= nums2[pointer2]):
                nums1[index] = nums1[pointer1]
                nums1[pointer1] = float('inf') # NOTE: Want to set it to inf so it doesnt affect future iterations (i.e the last iter)
                pointer1 += 1
            else: # pointer1 == m+n or nums1[pointer1] > nums2[pointer2]
                nums1[index] = nums2[pointer2]
                pointer2 += 1
            index += 1
            

        

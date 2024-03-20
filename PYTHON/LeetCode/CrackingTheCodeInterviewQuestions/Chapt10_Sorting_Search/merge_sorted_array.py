from typing import List
import sys


class Solution:
    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for index in range(len(nums2)):
                nums1[index] = nums2[index]
            return

        pointer_full = m + n - 1
        pointer_1 = m - 1
        pointer_2 = n - 1

        while pointer_1 >= 0 and pointer_2 >= 0:
            # 1 greater
            if nums1[pointer_1] > nums2[pointer_2]:
                nums1[pointer_full] = nums1[pointer_1]
                nums1[pointer_1] = None
                pointer_1 = pointer_1 - 1
            # 2 greater
            else:
                nums1[pointer_full] = nums2[pointer_2]
                pointer_2 = pointer_2 - 1
            pointer_full = pointer_full - 1

        if pointer_2 >= 0: # NOTE: This can be embedded in While loop see textbook solution
            while pointer_full >= 0:
                nums1[pointer_full] = nums2[pointer_2]
                pointer_2 = pointer_2 - 1
                pointer_full = pointer_full - 1

        return nums1



if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
    assert sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3) == [1,2,2,3,5,6]
    assert sol.merge([1], 1, [], 0) == [1]
    print(sol.merge([0], 0, [1], 1))
    assert sol.merge([0], 0, [1], 1) == [1]



            ## ATTEMPT TO SORT IN-PLACE. TOO COMPLOCATED START SIMPLE BC
            ## MODIFYING FROM LEFT TO RIGHT CAN LEAD TO BREAKING THE ORDERING
            ## NEED TO MAINTAIN INVARIANT THAT BOTH ARRAYS ARE SORTED
            # if nums1[pointer1] <= nums2[pointer2]:
            #     # 1 is smaller
            #     pointer1 = pointer1 + 1
            # else:
            #     # 2 is smaller
            #     # swap
            #     one = nums1[pointer1]
            #     nums1[pointer1] = nums2[pointer2]
            #     nums2[pointer2] = one
            #     pointer1 = pointer1 + 1
            #
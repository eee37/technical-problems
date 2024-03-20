'''
    Qs:
        Could I have done it w/o a helper fxn. Come up with a different recursive case

    TimeComplexity: O(N) -> where N is the size of the list
    SpaceComplexity: O(N)


    Improvement:
        Soln: CtCI Improves by creating recrusive fxn that returns root node and uses indices to determine base case(s)
'''

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @staticmethod
    def sortedArrayToBST(nums: List[int]) -> TreeNode:
        # base case
        if not nums:
            return None
        root = TreeNode(nums[len(nums)//2])
        # Call recursive fxn
        if len(nums) > 1:
            Solution.sortedArrayToBSTHelper(root, nums)
        return root

    @staticmethod
    def sortedArrayToBSTHelper(head: TreeNode, nums: List[int]):
        if len(nums) <= 1:
            return
        breakpoint = len(nums)//2
        left = nums[0:breakpoint]
        left_c =  TreeNode(left[len(left)//2]) if left else None
        head.left = left_c
        Solution.sortedArrayToBSTHelper(head.left, left)
        if len(nums) > 2: #case where 2 element array, no left child
            right = nums[breakpoint+1:]
            right_c =  TreeNode(right[len(right)//2]) if right else None
            head.right = right_c
            Solution.sortedArrayToBSTHelper(head.right, right)


if __name__ == '__main__':
    # Solution.sortedArrayToBST([-10,-3,0,5,9])
    # Solution.sortedArrayToBST([1,3])
    Solution.sortedArrayToBST([1])


class Solution2:
    def sortedArrayToBST(self,nums: List[int]) -> TreeNode:
        # base case
        if not nums:
            return None
        root = TreeNode(nums[len(nums)//2])
        # Call recursive fxn
        if len(nums) > 1:
            self.sortedArrayToBSTHelper(root, nums)
        return root
    def sortedArrayToBSTHelper(self, head: TreeNode, nums: List[int]):
        if len(nums) <= 1:
            return
        breakpoint = len(nums)//2
        left = nums[0:breakpoint]
        left_c =  TreeNode(left[len(left)//2]) if left else None
        head.left = left_c
        Solution.sortedArrayToBSTHelper(head.left, left)
        if len(nums) > 2: #case where 2 element array, no left child
            right = nums[breakpoint+1:]
            right_c =  TreeNode(right[len(right)//2]) if right else None
            head.right = right_c
            self.sortedArrayToBSTHelper(head.right, right)


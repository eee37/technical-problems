# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        left_st = False
        right_st = False
        if root:
            targetSum -= root.val
            if root.left:
                left_st = self.hasPathSum(root.left, targetSum)
            if not left_st and root.right:
                right_st = self.hasPathSum(root.right, targetSum)
            if root.left is None and root.right is None:
                return targetSum == 0
        return left_st or right_st

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        height = 0
        if root:
            height += 1
            l_height = self.maxDepthRecurse(root.left, height, height)
            r_height = self.maxDepthRecurse(root.right, height, height)
            height = max(l_height, r_height)
        return height

    def maxDepthRecurse(self, root: Optional[TreeNode], height:int, max_height: int) -> int:
        if root:
            height += 1
            if height > max_height:
                max_height = height
            l_height = self.maxDepthRecurse(root.left, height, max_height)
            r_height = self.maxDepthRecurse(root.right, height, max_height)
            max_height = max(l_height, r_height)
        return max_height

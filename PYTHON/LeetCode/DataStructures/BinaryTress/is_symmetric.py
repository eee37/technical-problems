# Definition for a binary tree node.
# and, or bool conditional operators
# self when using a method withing a method
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        is_symmetric = True
        if root:
            queue = []
            self.traverse_left(root.left, queue)
            is_symmetric = self.check_symmetry(root.right, queue)
        return is_symmetric

    def traverse_left(self, root: Optional[TreeNode], queue: List) -> None:
        if root:
            queue.append(root.val)
            self.traverse_left(root.left, queue)
            self.traverse_left(root.right, queue)
        else:
            queue.append(None)

    def check_symmetry(self, root: Optional[TreeNode], queue: List) -> None:
        if root:
            if root.val == queue.pop(0):
                r_sym = self.check_symmetry(root.right, queue)
                l_sym = self.check_symmetry(root.left, queue)
                return r_sym and l_sym
            else:
                return False
        else:
            if queue.pop(0) is None:
                return True
            else:
                return False

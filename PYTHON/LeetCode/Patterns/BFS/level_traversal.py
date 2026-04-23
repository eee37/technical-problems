"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
#102
    TIME: O(n) visiting every node
    SPACE: O(n) Worst case: last level has ~N/2 nodes
"""
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        q = deque([root] if root else []) # NOTE: need to explicitly sed to empty when none else get a [None]
        levels = []
        # level = 0

        while q:
            visited = []
            nxt_level = []

            for node in q: # NOTE: for _ in range(len(q)): iterating over the range would allow use to pop in loop
                visited.append(node.val)
                if node.left:
                    nxt_level.append(node.left)
                if node.right:
                    nxt_level.append(node.right)
            levels.append(visited) # NOTE visited is an array
            q = nxt_level # NOTE: KEY t this point we have processed all the nodes so can "reset." This allows as to avoid modifying q while looping over it
        return levels
            
            

        
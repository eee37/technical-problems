'''
    LC #272

    NOTES
        - My solution can be optimized by only storing k elements in heap
        - Approach 1 is clean
        - Approach 2 is cleaner more optimized version of my solution
        - Approach 3 uses Quickselect (https://en.wikipedia.org/wiki/Quickselect). Good problem to review
    
    Tags: #Review
'''

# Definition for a binary tree node.
from typing import List, Optional
from heapq import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        if not root:
            raise Exception('empty tree')

        lst_diff = []


        self.dfs(root, lst_diff, target)

        result = []

        while lst_diff and len(result) < k:
            tup = heappop(lst_diff)
            result.append(tup[1])

        return result





    def dfs(self, root: Optional[TreeNode], lst_diff: List[tuple], target: float):
        if not root:
            raise Exception('empty tree')

        heappush(lst_diff, (abs(root.val - target), root.val) )


        if root.left:
            self.dfs(root.left, lst_diff, target)

        if root.right:
            self.dfs(root.right, lst_diff, target)

if __name__ == "__main__":

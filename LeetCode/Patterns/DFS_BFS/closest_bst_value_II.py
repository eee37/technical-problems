'''
    LC #272

    NOTES
        - My solution can be optimized by only storing k elements in heap
        - Approach 1 is clean
        - Approach 2 is cleaner more optimized version of my solution
        - Approach 3 uses Quickselect (https://en.wikipedia.org/wiki/Quickselect). Good problem to review
        - Guide to QuickSelect
            0. Input to quickselect is start and end index
            1. Need a partition helper fxn that returns index of random element once sorted
            Inputs are random index and start and end index
            2. pick a random index and call partition on it
            3. partition will change ordering so that elements < element at random index are to the left and larger to the right 
                1. Partition does this by placing random element right most and using 2 pointers
                one (pt1) to scan the entire list 
                and the other (pt2) tracks the location is where the first largest element appears initiated at leftmost index
                2. Then the logic swaps and moves the index accordingly to keep invariant true
                    0. If element is less than random swap pt1 and pt2. Increment both
                    1. Only incrememt pt1 to find next smallest to swap with
                3. Finally swap random with pt2
                4. Return final index of random element
            4. If random element is at position k you are done otherwise focus in part of the array
            containing k use left, k, right to determine part to focus on
    
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

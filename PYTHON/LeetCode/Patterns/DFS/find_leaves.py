'''
******************* PROBLEM STATEMENT
LC # 366

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY:
SPACE COMPLEXITY:

******** SOLUTION

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* TAGS
#DFS
'''

# Definition for a binary tree node.
from ast import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Q: Can we assum tree nodes unique

n = # nodes
Time:  O(n). This is actually O(n logn) I think bc we need to perform DFS for each level. Optimal solution (solution 2) only scans the tree once
Space: O(n) if you count result ow O(logn)

Trick is that nodes are collected based on height where height is measured as distance to deepest leaf node

Optimal Solution essentially calculates the height in one pass and adds values to array based on height. 
Recursion and DP are used to calculate height
'''
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        def dfs(root: TreeNode, leafs: List[int]):
            if root.left is None and root.right is None:
                leafs.append(root.val)
                return True

            if root.left:
                left_leaf = dfs(root.left, leafs)
                if left_leaf:
                    root.left = None
            if root.right:
                right_leaf = dfs(root.right, leafs)
                if right_leaf:
                    root.right = None
            return False
        
        ans = []
        if root:
            while root.left or root.right:
                new_leafs = []
                dfs(root, new_leafs)
                ans.append(new_leafs)
            ans.append([root.val])
        
        return ans
            
            
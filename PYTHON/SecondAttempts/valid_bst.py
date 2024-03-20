'''
******************* PROBLEM STATEMENT
LC # 98

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY: O N
SPACE COMPLEXITY: O N (unbalanced) or O log N (balanced)

******** SOLUTION

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* TAGS
#BST #recursion
NOTE: 
    1. Recall definiton of BST extends to deep nested nodes
    2. Trick is to pass min and max value
        when you go left/right the max/min contraint becomes tighter
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import math
from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isValidBSTHelper(root, -math.inf, math.inf)
        
        
        
    def isValidBSTHelper(self, root:Optional[TreeNode], min_val: int, max_val: int) -> bool:
        if not root:
            return True
        if root.val > min_val and root.val < max_val:
            return self.isValidBSTHelper(root.left, min_val, root.val) and self.isValidBSTHelper(root.right, root.val, max_val)
        return False
        
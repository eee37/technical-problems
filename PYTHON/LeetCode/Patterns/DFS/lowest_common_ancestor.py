# Definition for a binary tree node.
# Is a path guaranteed to exist
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        hashmap = dict()
        lowest = math.max # TODO:
        def length_to_nodes(node, target):
            if not node:
                return -math.max # TODO:
            if node.val == target.val
                return 0
            nonlocal hashmap
            nonlocal lowest
            distance = 1 + length_to_nodes(node.left, p) + 1 + length_to_nodes(node.right, q)
            lowest = min(distance, lowest)
            hashmap[lowest] = node.val
            return distance
        min_distance = length_to_nodes(root, p) + 
        return hashmap[lowest]
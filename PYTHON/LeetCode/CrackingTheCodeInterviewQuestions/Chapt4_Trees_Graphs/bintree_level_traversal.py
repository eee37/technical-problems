from typing import List
'''
    CtCI Requests for linked list:
    instead would keep use array to keep track of tail nodes at each level
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        arr = [[root.val]]

        self.levelOrderTraversal(root, arr, 1, 'left')
        self.levelOrderTraversal(root, arr, 1, 'right')

        return arr

    @staticmethod
    def levelOrderTraversal(head, arr, depth, side):
        node = head.left if side == 'left' else head.right
        if node:
            # case where we are at this depth for the first time
            if len(arr) < depth + 1:
                arr.append([node.val])
            else:
                arr[depth].append(node.val)
            # recurse
            Solution.levelOrderTraversal(node, arr, depth + 1, 'left')
            Solution.levelOrderTraversal(node, arr, depth + 1, 'right')


solution = Solution()
root0 = TreeNode(20, TreeNode(15), TreeNode(7))
root1 = TreeNode(3, TreeNode(9), root0)
root2 = TreeNode(1)

solution.levelOrder(root0)
solution.levelOrder(root1)
solution.levelOrder(root2)
solution.levelOrder(None)
from DataStructures.treenode import insertLevelOrder
'''
     First solution failed to account for scenario where node in left subtree of root is right child of parent so greater than parent but also greater than root
    Hints: #35, #57, #86, # 113, # 128
    # 86
    If every node on the left must be less than or equal to the current node, then this is really
    the same thing as saying that the biggest node on the left must be less than or equal to
    the current node.
    
    
    Soln 1: Use in-order traversal to assure BST is in order (does not work when duplicates are allowed see soln for explanation). remember that in 
    a BST traversing a tree from leftmost to rightmost should return an ordered array
    
    NOTE: Code simpler if recursive call only looks at current node rather than children nodes

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @staticmethod
    def isValidBST(root: TreeNode) -> bool:
        min = -2**31 - 1
        max = 2**31 - 1
        return Solution.recursive_case(root, min, max)

    @staticmethod
    def recursive_case(root: TreeNode, min, max):
        if not root:
            return True
        if root.val < min or root.val > max:
            return False
        return Solution.recursive_case(root.left, min, root.val) and Solution.recursive_case(root.right, root.val, max)

    # @staticmethod
    # def isValidBST(root: TreeNode) -> bool:
    #     if not root:
    #         return True
    #
    #     return Solution.recursive_case(root, root.val, root.val)
    #
    # @staticmethod
    # def recursive_case(root: TreeNode, min, max):
    #     left, right = True, True
    #     if root.left:
    #         if root.left.val >= root.val or root.left.val < min:
    #             return False
    #         if root.left.val < min:
    #             min = root.left.val
    #         left = Solution.recursive_case(root.left, min, max)
    #     if root.right:
    #         if root.right.val <= root.val or root.right.val > max:
    #             return False
    #         if root.right.val > max:
    #             max = root.right.val
    #         right = Solution.recursive_case(root.right, min, max)
    #     return left and right

if __name__ == '__main__':
    # arr = [2,1,3]
    # root = insertLevelOrder(arr, None, 0, len(arr))
    # print(Solution.isValidBST(root))
    #
    # arr = [5,1,4,None,None,3,6]
    # right = TreeNode(4, TreeNode(3), TreeNode(6))
    # root = TreeNode(5, TreeNode(1), right)
    # # root = insertLevelOrder(arr, None, 0, len(arr)) # NOTE: insertLevelOrder for None (no chiled nodes) creates child nodes with value None
    # print(Solution.isValidBST(root))

    right = TreeNode(6, TreeNode(3), TreeNode(7))
    root = TreeNode(5, TreeNode(4), right)
    # root = insertLevelOrder(arr, None, 0, len(arr)) # NOTE: insertLevelOrder for None (no chiled nodes) creates child nodes with value None
    print(Solution.isValidBST(root))

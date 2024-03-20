from DataStructures.treenode import insertLevelOrder
'''
    NOTE: Solutions says heights of any node may not differ by > 1 meaning that root node can be balanced but nested nodes not
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # # TRY # 1
    # def isBalanced(self, root: TreeNode) -> bool:
    #     if not root:
    #         return True
    #     if not root.left and not root.right:
    #         return True
    #     left_height = self.get_max_depth(root.left, 1)
    #     right_height = self.get_max_depth(root.right, 1)
    #     return True if abs(left_height - right_height) <=1 else False
    @staticmethod
    def isBalanced(root: TreeNode) -> bool:
        # base case
        if not root:
            return True
        if not root.left and not root.right:
            return True
        count_left = Solution.helper(root.left, 0)
        count_right = Solution.helper(root.right, 0)
        return True if abs(count_left - count_right) <= 1 else False

    @staticmethod
    def helper(root: TreeNode, count: int) -> int:
        # base case # 1
        if not root:
            return count
        # case 1 both null. base case # 2
        if not root.left and not root.right:
            return count + 1
        # case 2 only left null
        if not root.left and root.right:
            return Solution.helper(root.right, count + 1)
        # case 3 only right null
        if root.left and not root.right:
            return Solution.helper(root.left, count + 1)
        # case 4 both not null
        return max(Solution.helper(root.right, count + 1), Solution.helper(root.left, count + 1))

    @staticmethod
    def get_max_depth(node: TreeNode, depth: int) -> int:
        if node:
            if not node.left and not node.right:
                return depth
            else:
                left_height = Solution.get_max_depth(node.left, depth + 1)
                right_height = Solution.get_max_depth(node.right, depth + 1)
            return max(left_height, right_height)
        else:
            return depth # is this correct?


def preOrder(root):
    if root != None:
        print(root.data, end="\n")
        preOrder(root.left)
        preOrder(root.right)

if __name__ == '__main__':
    sol = Solution()

    # arr = [3,9,20,None,None,15,7]
    # root = insertLevelOrder(arr, None, 0, len(arr))
    #
    # print(sol.isBalanced(root))

    # arr = [1,2,2,3,3,None,None,4,4]
    # root = insertLevelOrder(arr, None, 0, len(arr))


    # NOTE: None is inserting NODES with all props as None

    # root = TreeNode(1)
    # print(sol.isBalanced(root))
    #
    # print(sol.isBalanced(None))

    # root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    # print(sol.isBalanced(root))

    arr = [1,2,2,3,3,None,None,4,4]
    root = insertLevelOrder(arr, None, 0, len(arr))
    print(sol.isBalanced(root))


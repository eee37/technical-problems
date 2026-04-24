# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        def find_path(node, curr_sum, targetSum):
            if not node:
                return (False, [])
            # root
            curr_sum += node.val
            if not node.left and not node.right:
                if curr_sum == targetSum:
                    return (True, [[node.val]])
                else:
                    return (False, [])
            left_tup = find_path(node.left, curr_sum, targetSum)
            right_tup =  find_path(node.right, curr_sum, targetSum)
            true_paths = []
            if left_tup[0]:
                for path in left_tup[1]:
                    path.append(node.val)
                    true_paths.append(list(path))
            if right_tup[0]:
                for path in right_tup[1]:
                    path.append(node.val)
                    true_paths.append(list(path))
            if true_paths:
                return (True, true_paths)
            return (False, [])
        result = find_path(root, 0, targetSum)
        # NOTE: Answer expects it ordered from root to leaft
        for path in result[1]:
            path.reverse()
        return result[1]

# from collections import deque
# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution(object):
#     def pathSum(self, root, targetSum):
#         """
#         :type root: Optional[TreeNode]
#         :type targetSum: int
#         :rtype: List[List[int]]
#         """
#         if not root:
#             return []

#         def find_path(node, curr_sum, targetSum):
#             if not node:
#                 return (False, [])
#             # root
#             curr_sum += node.val
#             if not node.left and not node.right:
#                 if curr_sum == targetSum:
#                     queue = deque([node.val])
#                     return (True, [queue])
#                 else:
#                     return (False, deque([]))
#             left_tup = find_path(node.left, curr_sum, targetSum)
#             right_tup =  find_path(node.right, curr_sum, targetSum)
#             true_paths = []
#             if left_tup[0]:
#                 for path in left_tup[1]:
#                     path.appendleft(node.val)
#                     true_paths.append(deque(path))
#             if right_tup[0]:
#                 for path in right_tup[1]:
#                     path.appendleft(node.val)
#                     true_paths.append(deque(path))
#             if true_paths:
#                 return (True, true_paths)
#             return (False, [])
#         result = find_path(root, 0, targetSum)
#         # NOTE: Answer expects it ordered from root to leaft
#         print("result", result)
#         return [list(path) for path in result[1]]
        
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def zigzagLevelOrder(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: List[List[int]]
#         """
#         if not root:
#             return []
#         result = []
#         queue = deque([root])
#         left_to_right = False
#         while queue:
#             print("-----------------------------")
#             print("queue", queue)
#             print("result", result)
#             # NOTE: LEVEL OPERATIONS HAPPEN OUTSIDE THE FOR LOOP
#             result.append([])
#             left_to_right = not left_to_right
#             lvl_length = len(queue)
#             for index in range(len(queue)):
#                 print("_", index)
#                 print("left_to_right", left_to_right)
#                 nxt = queue.popleft()
#                 print("nxt", nxt)
#                 if nxt.left:
#                     queue.append(nxt.left)
#                 if nxt.right:
#                     queue.append(nxt.right)
#                 result[len(result)-1].append(nxt.val)
#             if not left_to_right:
#                 result[len(result)-1].reverse() # NOTE: This is an expensive task as it takes O(n) in works case scenario and we are doing it at every level
#         return result



# from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = [root]
        level = 0 
        while queue:
            print("-----------------------------")
            print("queue", queue)
            print("result", result)
            print("level", level)
            # NOTE: LEVEL OPERATIONS HAPPEN OUTSIDE THE FOR LOOP
            result.append([])
            lvl_length = len(queue)
            for index in range(len(queue)):
                print("_", index)
                nxt = None
                if level % 2  == 0:
                    nxt = queue.pop(0)
                else:
                    nxt = queue.pop(lvl_length-1-index)
                print("nxt", nxt)
                if nxt.left:
                    queue.append(nxt.left)
                if nxt.right:
                    queue.append(nxt.right)
                result[len(result)-1].append(nxt.val)
            level += 1
        return result



        

        
        
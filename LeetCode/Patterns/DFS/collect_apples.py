'''
******************* PROBLEM STATEMENT
LC # 1443

******************* NOTES
Didn't solve
Trick was to start summing distance at the deepest level. summing starts at deepest stack call and bubbles up
Return to # TODO: Salesforce
******** MY IMPLEMENTATION:

TIME COMPLEXITY:
SPACE COMPLEXITY:

******** SOLUTION

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* TAGS
#dfs
'''


'''
    QUESTIONS:
        1. Can I assume left childs always preceed right child. Assuming yes
    TODO: Read artical about variable scope again
    Not getting correct answer. Debug with debugger to see if I am creating graph correctly
    Maybe I am no creating graph right
    
    https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/discuss/624141/Clean-Python-3-peel-onion-in-O(N)-100-timespace
    https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/discuss/623673/Concise-explanation-with-a-Picture-for-Visualization
'''
from typing import List


class Node:
    def __init__(self, id):
        self.id = id
        self.l = None
        self.r = None
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # TREE TRAVERSAL
        nodes =  {id: Node(id) for id in range(n)}
        
        for edge in edges:
            to_id, fr_id = edge
            to_node = nodes[to_id]
            fr_node = nodes[fr_id]
            if to_node.l is None:
                to_node.l = fr_node
            else:
                fr_node.r = fr_node
                
        
        def tree_traversal(start: Node, depth: int, output: 0) -> bool:
            left_app = False
            right_app = False
            print(f'APPLE {start.id} {output}')
            if start.l:
                left_app, amount  = tree_traversal(start.l, depth + 1, output)
                output += amount
            
            if start.r:
                right_app, amount = tree_traversal(start.r, depth + 1, output)
                output += amount
            
            if (hasApple[start.id] or left_app or right_app) and depth != 0: # NOTE: Adding at destination node
                output += 2
                print(f'----RED APPLE {start.id} {output}')
            
            return (hasApple[start.id] or left_app or right_app, output)  # NOTE: We want to know if any of that tress ancestors have a apple not just that tree
        
        return tree_traversal(nodes[0], 0, 0)[1]
'''
******************* PROBLEM STATEMENT
LC # 399
Link: https://leetcode.com/problems/evaluate-division/

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY:
SPACE COMPLEXITY:

******** SOLUTION

TIME COMPLEXITY: O(M*N) where M is num equations and N is num queries

Note that graph creation is O(M)
Driver of time complexity is second step cuz for each query we are traversing possibly the entire graph
Note that the graph traversal grows in respect to the num of equations since equations symbolize edges
an addition edge means an additional traversal
SPACE COMPLEXITY:
    O(M) or O(M+ N) if you include space required to store result. The N comes from the space required to store result as it grows in respect to num queries
Note that number of equations is proportional to max number of nodes so M equations implies a max of 2M nodes
We build a graph out the equations. In the worst case where there is no overlapping among the equations, 
we would have NN edges and 2N2N nodes in the graph. Therefore, the sapce c
omplexity of the graph is \mathcal{O}(N + 2N) = \mathcal{O}(3N) = \mathcal{O}(N)O(N+2N)=O(3N)=O(N).


******************* TAGS
'''

from typing import List
from collections import defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.child_dict = defaultdict(lambda: Node) # { "child": weight }

    def add_child(self, node, val):
        self.child_dict.update({node : val})


class Solution:
    '''
        NOTE: BFS is not a good solution here bc the path is important. Want to have previously visited nodes quickly accessible
    def bfs(self, start, end):
        queue = [(n, w) for n, w in start.child_dict.items()] # TODO: Check
        visited = set()
        whilte queue:
            nxt = queue.pop(0)
            if nxt.val in visited:
                continue
            visited.add(nxt.val)
            for neighbor in nxt.child_dict.items():
                queue.append(neighbor)
    '''

    def dfs(self, curr, end, visited, ans):
        if curr.val == end.val: 
            return ans

        visited.add(curr.val)

        for n, w in curr.child_dict.items():
            if n.val in visited:
                continue
            new_ans = self.dfs(n, end, visited, ans * w) # NOTE: Needed to name output new name not ans bc it can overwrite ans value in the case it returns -1
            if new_ans != -1: # NOTE: Don't need to expore remaning childrent of current node. Propegate solution to top stack
                return new_ans

        return -1





    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodes = defaultdict(lambda: None)

        # CREATE GRAPH
        for index, e in enumerate(equations):
            a = e[0]
            b = e[1]

            if nodes[a] is None:
                new_node = Node(a)
                nodes.update({a: new_node})
                # new_node.add_child(new_node, 1)


            if nodes[b] is None:
                new_node = Node(b)
                nodes.update({b: new_node})
                # new_node.add_child(new_node, 1)

            node_a = nodes[a]
            node_b = nodes[b]

            node_a.add_child(node_b, values[index])
            node_b.add_child(node_a, 1/values[index])

        # CALCULATIONS
        result = []

        for q in queries:
            start_node = nodes[q[0]]
            end_node = nodes[q[1]]

            # Edge cases
            if start_node is None or end_node is None:
                result.append(-1)
                continue

            if start_node.val == end_node.val:
                result.append(1)
                continue


            # Look for path. Need to use DFS
            ans = self.dfs(start_node, end_node, set(), 1)
            result.append(ans)

        return result

sol = Solution()

print(sol.calcEquation([["a","b"],["b","c"]], 
                        [2.0,3.0], 
                        [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))



print(sol.calcEquation([["a","b"],["b","c"],["bc","cd"]],
                        [1.5,2.5,5.0],
                        [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))


print(sol.calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]],
                        [3.0,4.0,5.0,6.0],
                        [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]))
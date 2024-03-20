from typing import List

'''
******************* PROBLEM STATEMENT
LC # 797
Link: https://leetcode.com/problems/all-paths-from-source-to-target/

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY: On
SPACE COMPLEXITY: On

******** SOLUTION

TIME COMPLEXITY:
SPACE COMPLEXITY:

NOTE: Ap. Need to use DFS because we care about the path to the current node. In BFS
this becomes harder bc we dont traverse a whole path from beginning to end in a single go

- Approach 1: Backtracking. Pops added elements after call stack ended to avoid re-creating a new path every time
- Good problem to review On (Con),
- DP approach very hard to understand 
******************* TAGS
'''

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # BFS
        if not graph or len(graph[0]) == 0:
            return []
        
        def dfs(cur: int, path: List[int], graph: List[List[int]], result: List[List[int]]):
            path = path + [cur] # NOTE: Con  Can't just append to path bc then all stack traces will point to same var. Need to be smart about when reusing a var or mutating it vs creating a new var. Recursion issue
            
            if cur == len(graph) - 1:
                result.append(path)
                return # NOTE: No cycles cant point back to final
            
            nxt = graph[cur]
            
            for node in nxt:
                dfs(node, path, graph, result)
        
        result = []
        dfs(0, [], graph, result)
        
        return result
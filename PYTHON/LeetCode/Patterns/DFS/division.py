'''
******************* PROBLEM STATEMENT
LC # 399

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY:
SPACE COMPLEXITY:

******** SOLUTION

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* TAGS
#DFS #Graph
'''

'''
    Notes:
        - Took way too long
        - Did not get an answer one test case failing
'''
from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        default = lambda: None
        g = defaultdict(lambda: defaultdict(default)) # Os(N)

        # create graph
        for index, pair in enumerate(equations): # <= Ot(N) where n is all nodes
            to = pair[0]
            fr = pair[1]
            to_dict = g[to]
            from_dict = g[fr]

            to_dict.update({fr: values[index]})
            if values[index] != 0:
                from_dict.update({to: 1/values[index]})

            to_dict.update({to: 1})
            from_dict.update({fr: 1})
            

        response = []



        for q in queries: # == Ot(N) where n is all nodes bc dfs is what drives time complexity
            to = q[0]
            fr = q[1]

            # do both exist in g
            if len(g[to]) == 0 or len(g[fr]) == 0: #
                response.append(-1)
                continue

            # direct path already exists
            if g[to][fr] is not None:
                response.append(g[to][fr])
                continue
            else:
                # add reachable nodes from to
                self.dfs(to, to, g) # failing here

            if g[to][fr] is not None:
                response.append(g[to][fr])
                continue # NOTE: _ can be dangerous to use continue. if forgotten causes bugs
            response.append(-1)




        return response

    # NOTE: _ This leads to a infinite loop. Can revisit visited nodes. Solution would need to prevent from revisting nodes
    def dfs(self, start: str, curr: str, g, ans = 1, visited = set() ) -> int: # Return to. How to denote dict type. == Ot(N) where n is all nodes

        visited.add(curr)

        for key, val in g[curr].items(): 
            if key == curr or key == start:
                continue
            if g[start][key] is None:
                g[start].update({key: ans * val})
                g[key].update({start: 1/(ans * val)})
            if key not in visited:
                self.dfs(start, key, g, ans * val)



        # for key, val in g[curr].items(): 
        #     if key == curr or key == start:
        #         continue

        #     if (ans * val) != 0 and g[start][key] is None: # Add to Only dig deeper in unexplored territory?
        #         g[start].update({key: ans * val})
        #         g[key].update({start: 1/(ans * val)})
        #         if key not in visited:
        #             self.dfs(start, key, g, ans * val)



sol = Solution()

# print(sol.calcEquation([["a","b"],["b","c"]], 
#                         [2.0,3.0], 
#                         [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))



print(sol.calcEquation([["a","b"],["b","c"],["bc","cd"]],
                        [1.5,2.5,5.0],
                        [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
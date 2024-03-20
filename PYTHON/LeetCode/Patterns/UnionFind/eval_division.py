from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        node_parent = defaultdict(lambda: None)
        def find(val, weight = 1): # Tricky to pass weight and re-calculate weight
            if node_parent[val] is None:
                node_parent.update({val: dict({'parent': val, 'weight': 1})})
            if node_parent[val]['parent'] != val:
                # assign correct parent
                # CHECK new weight being assign correctly
                node_parent[val]['parent'], node_parent[val]['weight']  = find(node_parent[val]['parent'], weight * node_parent[val]['weight']) # NOTE: LESSON 1 Solution does not pass weight. It calculares new weight via backtracking. the last returned weight will be old root/ new root and current weight is current/old root. Weight backtracks
            return (node_parent[val]['parent'], weight)

        def union(top, bottom, weight):
            t_parent = find(top)[0]
            b_parent = find(top)[0]

            if t_parent == b_parent:
                return
            else:
                # Assign root of bottom to be top. CHECK
                # NOTE: Lesson 2 we are merging top's set with bottom's set. This means getting the root of top and pointing it to bottom or bottom's root
                node_parent[top]['parent'] = bottom
                node_parent[top]['weight'] = weight 
            

        # Construct UnionFind

        for index,e in enumerate(equations):
            union(e[0], e[1], values[index])
        results = []

        for q in queries:
            if node_parent[q[0]] is None or node_parent[q[1]] is None:
                results.append(-1)
                continue
            t_parent, t_w = find(q[0])
            b_parent, b_w = find(q[1])
            if t_parent != b_parent:
                results.append(-1)
                continue
            else:
                results.append(t_w/b_w)
        
        return results
            


from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        node_parent = defaultdict(lambda: None)
        def find(val): # Tricky to pass weight and re-calculate weight
            if node_parent[val] is None:
                node_parent.update({val: dict({'parent': val, 'weight': 1})})
            
            info = node_parent[val]
            parent = info['parent'] # root is more appropriate name than parent
            weight = info['weight']

            if parent != val:
                # assign correct parent
                # CHECK new weight being assign correctly
                root, parent_weight  =  find(parent) # NOTE: Solution does not pass weight
                node_parent[val] = dict({'parent': root, 'weight': weight * parent_weight})
            return (node_parent[val]['parent'], weight)

        def union(top, bottom, weight):
            t_parent, t_w = find(top)
            b_parent, b_w = find(top)

            if t_parent == b_parent:
                return
            else:
                # Assign root of bottom to be top. CHECK
                # Lesson 2: NOTE: The node who we are adjusting is top's root node (see Union Find algo) to point to bottoms root node. We want tops root node weight to be ratio of its weight to bottom's root node
                node_parent[t_parent]['parent'] = b_parent
                node_parent[t_parent]['weight'] = (weight * b_w/t_w) # top = a, top root = c, bottom = b, bottom root = d, we want, top root/bottom_root = c/d                      
            

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
            


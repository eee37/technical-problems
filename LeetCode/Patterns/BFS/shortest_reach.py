'''
******************* PROBLEM STATEMENT
LC # ___

******************* NOTES

NOTE: Failing for some long test cases. Not clear why
******** MY IMPLEMENTATION:

TIME COMPLEXITY:
SPACE COMPLEXITY:

******** SOLUTION

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* TAGS
'''


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n = num nodes
#  2. INTEGER m = num edges
#  3. 2D_INTEGER_ARRAY edges = edges
#  4. INTEGER s = stert
#

class Node:
    def __init__(self, val):
        self.val = val
        self.chil = []
    
    def add_child(self, child):
        self.chil.append(child)

def bfs(n, m, edges, s):
    # STEP 1: Create graph
    nodes = dict()
    
    for num in range(1, n+1):
        nodes.update({num: Node(num)})
    
    # remember edges are bi-directional
    for edge in edges:
        a = nodes[edge[0]]
        b = nodes[edge[1]]
        
        a.add_child(b)
        b.add_child(a)
    
    print(nodes)
    
    # STEP 2: Calculate result
    result = [-1] * n
    
    start = nodes[s]
    
    queue = []
    
    for node in start.chil:
        queue.append( (node, 6) )
    
    visited = set()
    
    while queue:
        nxt = queue.pop(0)
        node = nxt[0]
        dist = nxt[1]
        visited.add(node.val)
        print(result)
        print(node.val)
        result[node.val - 1] = dist
        
        for c in node.chil:
            if c.val not in visited:
                queue.append( (c, dist + 6) )
    
    # remove start node from result
    result.pop(s-1)
    return result
        
        
        
    
    
    
    
    
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

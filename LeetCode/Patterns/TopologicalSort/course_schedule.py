'''
******************* PROBLEM STATEMENT
Approach #3:

Topological Sort: Way of finding cycles
IDEA:
Create data strucuture to track dependency in this case dictionary {key-> course_id: value->{outNodes: a list of courses that have it as pre-req, inDegrees}}
Start at nodes with in degree = to 0
Start eliminationg out-going connections and decreasing in-degrees of nodes accordingly
if a inDegress becomes 0 add to list of nodes to check
if by the end the # of connections deleted is not equall to the total number of connections a cycle exists

Essentially the algo deletes relationships that are not in a cycle if by the end connections remain then they are acyclic (helps to draw connections and examples on paper)

******************* NOTES

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* SOLUTION
Questions
    1. Are all courses unique. i.e 1 represents one course
    2. Are pre-req always going to be of size 2
'''
from typing import List
from collections import defaultdict


class Solution:
    class Node: # NOTE: Could use arraylist instead of node
        def __init__(self, v=None):
            self.v=v
            self.c=[]
        def add_child(self, c):
            self.c.append(c)

    '''
    Uses DFS
    '''
    def is_cycle(self, num, checked, visited, prereq):
        if checked[num]:
            return False
        if visited[num]:
            return True

        visited[num] = True
        has_cycle = False
        for c in prereq[num]:
            has_cycle = self.is_cycle(c, checked, visited, prereq)
            if has_cycle:
                break
        if has_cycle:
            return True
        visited[num] = False
        checked[num] = True # NOTE: Node has been visited
        return False



    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adjancy list
        prereq = defaultdict(list)
        for req in prerequisites:
            children = prereq[req[0]]  # NOTE: w/ default dict calling get on an unknown key still returns None. Need to index to get default value
            children.append(req[1])
            prereq.update({req[0]: children})

        # check for cycle
        checked = [False] * numCourses
        visited = [False] * numCourses

        for num in range(numCourses):
            if not checked[num]:
                if self.is_cycle(num, checked, visited, prereq):
                    return False
        return True




    '''
        Issue is that we are only adding nodes w/ pre-reqs to the array. In the example below 0 is not in the dict
    '''
    def canFinishII(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create dictionary
        node_dict = dict()
        for pair in prerequisites:
            node = node_dict.get(pair[0])
            if node is None:
                node = self.Node(pair[0])
                node_dict.update({pair[0]: node})
            node.add_child(pair[1])

        # detect cycles
        for key, node in list(node_dict.items()): # NOTE: This returns (key, value) pairs
            visited = [0] * numCourses
            to_vist = [node]
            # BFS
            while len(to_vist) > 0:
                curr = to_vist.pop(0)
                if visited[curr.v] == 1:
                    return False
                visited[curr.v] += 1
                for c in curr.c:
                    if node_dict.get(c): # Don't want to repeat visits?
                        to_vist.append(node_dict.get(c)) # NOTE: to_visit is an array of nodes
        return True


if __name__ == '__main__':
    sol = Solution()
    assert sol.canFinish(2, [[1,0]])
    assert not sol.canFinish(2, [[1,0],[0,1]])
    assert sol.canFinish(8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]])







# DFS
from collections import defaultdict

from DataStructures.graphnode import GraphNode


# solution uses a dict [key]: list to represent graph where key represents a node and the list is a list of nodes connected to the key node

# NON ADJACENCY LIST approach
# def depth_search(value: int, node: GraphNode, visited=set()):
#     if value == node.value:
#         return value
#     else:
#         visited.add(value)
#     for child in node.chil:
#         if child.value not in visited:
#             depth_search(value, child, visited)

class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # ****************************************** DFS **********************************************************************
    # A function used by DFS
    def DFSUtil(self, v, visited): # NOTE: This is where we actually visit each node. Will be called on each node
        visited.add(v)
        print(str(v) + ' ')
        for chil in self.graph[v]:
            if chil not in visited:
                self.DFSUtil(chil, visited)


    # The function to do DFS traversal. It uses
    # recursive DFSUtil()

    def DFS(self):
        visited = set()

        for node in self.graph.keys():
            if node not in visited:
                self.DFSUtil(node, visited)

    # ****************************************** BFS **********************************************************************

    def BFS(self, start):
        queue = [start]
        visited = set()
        while queue:
            current = queue.pop(0) # NOTE: By default pop removes last element (-1) in array but can pass param to indicate which indice to pop
            visited.add(current)
            print(current)
            for chil in self.graph[current]:
                if chil not in visited:
                    queue.append(chil)



# Bi-directional Search??

if __name__ == '__main__':
    # g = Graph()
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(1, 2)
    # g.addEdge(2, 0)
    # g.addEdge(2, 3)
    # g.addEdge(3, 3)
    #
    # #0 -> 1, 2
    # #1 -> 2
    # #2 -> 0, 3
    # #3 -> 3
    #
    # print("Following is Depth First Traversal")
    # g.DFS()

    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 4)

    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.BFS(2)
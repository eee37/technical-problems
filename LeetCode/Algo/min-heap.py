# Skipping for time's sake

from DataStructures.treenode import BinaryTreeNode
import sys

# Min Heap. See https://www.geeksforgeeks.org/min-heap-in-python/
class MinHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1) # GeeksForGeeks uses an array to capture heap
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

## Insert
    def insert(self, element: int):
        pass
        # navigate to bottom-right most node
        # insert node
        # place node in location so as to satisfy min heap property
        # compare with parent node and replace if smaller
## Delete Min
    def remove(self):
        pass
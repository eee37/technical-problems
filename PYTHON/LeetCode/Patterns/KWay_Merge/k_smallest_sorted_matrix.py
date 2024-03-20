from typing import List
from heapq import *
'''
    NOTE: My solution runs too long. Probably bc of the check to make sure index tuple hasn't already been added
    Approach 1:
        * To undertand time complexity note that initializing the heap is not the same as inserting into heap since column is already sorted
        "The elements inserted in the first for loop are already sorted because they're coming from the first column in the matrix. And when the input is already sorted, the time complexity for N elements insertion in min heap is O(N)." 
    Approach 2: Is much less intuitive. It's a spin on binary search
'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        x = min(len(matrix[0]), k) # NOTE: Can't chop off last N -k columns when k is smaller than N
        heap = [(x, 0, col) for col, x in enumerate(matrix[0][:x])] # NOTE: for index, var
        smallest = None

        while k > 0:
            smallest = heappop(heap)
            k -= 1

            row = smallest[1]

            if row + 1 < len(matrix):
                r = smallest[1] + 1
                c = smallest[2]
                heappush(heap, (matrix[r][c], r, c))
        if smallest:
            return smallest[0]
        return smallest


    def kthSmallestNonOptimal(self, matrix: List[List[int]], k: int) -> int:
        sorted = []
        heap = []
        visited = [] # NOTE: need to keep track of visited to prevent visiting twice. visited are notes that have been pushed to prevent being pushed again

        if k > len(matrix)**2:
            return

        heappush(heap, (matrix[0][0], 0, 0))

        while len(sorted) < k and len(heap) > 0:
            tup = heappop(heap)
            sorted.append(tup[0])


            if tup[1] + 1 < len(matrix) and (tup[1] + 1, tup[2]) not in visited:
                heappush(heap, (matrix[tup[1] + 1][tup[2]], tup[1] + 1, tup[2]))
                visited.append((tup[1] + 1, tup[2]))
            if tup[2] + 1 < len(matrix) and (tup[1], tup[2] + 1) not in visited:
                heappush(heap, (matrix[tup[1]][tup[2] + 1], tup[1], tup[2] + 1))
                visited.append((tup[1], tup[2] + 1))
        return sorted[k-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8) )
    assert sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8) == 13
    assert sol.kthSmallest([[1,3,5],[6,7,12],[11,14,14]], 6) == 11
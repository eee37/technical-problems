"""
 TIME: O(nlogk)
 SPACE: O(k)

"""
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, lambda pt: (pt[0]**2 + pt[1]**2)**0.5)

        
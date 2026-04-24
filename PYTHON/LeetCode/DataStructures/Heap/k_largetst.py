import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums).pop() # NOTE: nlargest or nsmallest return a list of size

        
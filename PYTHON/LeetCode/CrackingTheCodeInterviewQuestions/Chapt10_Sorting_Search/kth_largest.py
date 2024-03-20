# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Implement KthLargest class:
#
# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

# IDEA: Use min-heap and maintain at size k (k max element will be min) bc fetching min in min-heap is O(1). Insertion is O(logk)
# Solution uses heapq rather than implementing own heap from scratch
from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) < self.k:
            return None
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


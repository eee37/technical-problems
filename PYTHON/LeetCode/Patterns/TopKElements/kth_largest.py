'''
******************* PROBLEM STATEMENT

******************* NOTES
1. heapq methods edit heap in place
2. random library for random numbers, selection: https://docs.python.org/3/library/random.html

TIME COMPLEXITY: O(NlogN)
SPACE COMPLEXITY: O(1)

******************* SOLUTION
1) My solution is most similar to Approach #2 but slightly less optimal (O(NlogN) vs O(NlogK). Approach 2 improves by only
storing largest K so that min is the smallest in heap. Note my original solution uses no storage but approach 2 does bc use
nlargest which creates a new list of size k
2) Optimal sol'n uses QuickSelect Algo which produces better runtime of O(n). See: https://en.wikipedia.org/wiki/Quickselect

'''

from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) # NOTE: Heapify transforms into heap in place
        # kth largest = n-k smallest
        # for i in range(len(nums) - k):
        #     heapq.heappop(nums) # NOTE: Takes heap as input
        # return nums[0] # Next up is kth largest

        return heapq.nlargest(k, nums)[-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.findKthLargest([3,2,1,5,6,4], 2))
    assert sol.findKthLargest([3,2,1,5,6,4], 2) == 5



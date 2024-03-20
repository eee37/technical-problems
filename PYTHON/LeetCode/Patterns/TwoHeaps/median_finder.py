'''
******************* PROBLEM STATEMENT

******************* NOTES

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* SOLUTION
'''
from heapq import *

'''
Brute Force: keep an array to store all added numbers. Knowing length can calculate median. Note this requires constantly sorting the array. In-efficient to much rework
Idea # 1: Keep two min heaps

2-Heaps Solution:
    https://leetcode.com/problems/find-median-from-data-stream/discuss/74047/JavaPython-two-heap-solution-O(log-n)-add-O(1)-find
    Solution provided here is very clean. Exploits the idea that in every scenario you can always add and remove from opposite heap (net 0 increase) and add one to correct heap (net 1)
    thus eliminating need to do a bunch of checks to determine where to add

'''


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = []  # max heap
        self.hi = []  # min heap
        self.count = 0

    def addNum(self, num: int) -> None:
        if self.count == 0:
            heappush(self.hi, num)
        elif self.count % 2 == 0:  # EVEN -> ODD
            if num >= -1 * self.lo[0]: # NOTE: Conditional statement to be in upper half it just needs to be larger than largest of lower half
                heappush(self.hi, num)
            else:  # NOTE: lo size changes are -1 + 1 =0, hi size change are +1
                lo_med = heappop(self.lo)
                if lo_med:
                    heappush(self.hi, -1 * lo_med)
                heappush(self.lo, -1 * num)
        else:  # ODD -> EVEN
            if num <= self.hi[0]: # NOTE: Conditional statement to be in lower half it just needs to be smaller than smallest of lower half
                heappush(self.lo, num * -1)
            else:
                hi_med = heappop(self.hi)
                if hi_med:
                    heappush(self.lo, -1 * hi_med)
                heappush(self.hi, num)
        self.count += 1

    def findMedian(self) -> float:
        if self.count == 0:
            return None
        elif self.count % 2 == 0:
            return float(self.hi[0] + self.lo[0] * -1) / 2
        else:
            return float(self.hi[0]) # NOTE: Wrapped in float fxn to conver to float



# Your MedianFinder object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(40)
    obj.addNum(12)
    obj.addNum(16)
    obj.addNum(14)
    obj.addNum(35)
    param_2 = obj.findMedian()
    assert param_2 == 6, print(param_2)

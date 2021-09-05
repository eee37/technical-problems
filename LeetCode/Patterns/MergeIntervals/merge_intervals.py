'''
******************* PROBLEM STATEMENT

******************* NOTES
# NOTE: (1) sort is a list method, (2) key flag can be used to pass lambda fxn that
# NOTE: min and max are build-in fxns no need to import
# NOTE: Don't want to edit list in place as we are currently looping over it. could lead to issues with index
# NOTE: Python lists have a built-in list.sort() method that modifies the list in-place. There is also a sorted() built-in function that builds a new sorted list from an iterable.
TIME COMPLEXITY: O(NLOGN)
SPACE COMPLEXITY: O(N), Note that sorting was done in place so did not require extra space
LINKS:
https://docs.python.org/3/howto/sorting.html

Leetcode solution is much simpler. Uses merged for all comparisons.
# NOTE: array[-1] ruturns last element in array
******************* SOLUTION

'''
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort
        intervals.sort(key=lambda interval:interval[0]) # NOTE: (1) sort is a list method, (2) key flag can be used to pass lambda fxn that defines how to sort

        new_intervals = []
        # compare and merge
        for index, curr in enumerate(intervals):
            if index > 0:
                # current starts before prev ends so they overlap, needs to be merged
                prev = intervals[index-1]
                if curr[0] <= prev[1]:
                    # curr = [math.min(prev[0], curr[1]), math.max(prev[0], curr[1])]
                    new_intervals.pop() # just merged with prev interval
                    new_interval = [min(prev[0], curr[0]), max(prev[1], curr[1])]
                    new_intervals.append(new_interval) # NOTE: min and max are build-in fxns no need to import
                    intervals[index] = new_interval # NOTE: want the next interval to be compared against range of new merged interval
                    # NOTE: Don't want to edit list in place as we are currently looping over it. could lead to issues with index
                else:
                    new_intervals.append(curr)
            else:
                new_intervals.append(curr)
        return new_intervals


class Solution:
    def mergeLeetcode(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort
        intervals.sort(key=lambda interval:interval[0]) # NOTE: (1) sort is a list method, (2) key flag can be used to pass lambda fxn that defines how to sort

        merged = []
        for inter in intervals:
            if not merged or inter[0] > merged[-1][1]:
                merged.append(inter)
            else:
                merged[-1][1] = max(merged[-1][1], inter[1])
        return merged
if __name__ == '__main__':
    sol = Solution()
    print(sol.mergeLeetcode([[1,3],[2,6],[8,10],[15,18]]))
    assert sol.mergeLeetcode([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert sol.mergeLeetcode([[1,4],[4,5]]) == [[1,5]]
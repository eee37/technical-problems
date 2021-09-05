'''
******************* PROBLEM STATEMENT

******************* NOTES
# NOTE: Don't need this as there shouldn't be more than 1 meeting w/ the same start time as another

TIME COMPLEXITY: O(NLOGN)
SPACE COMPLEXITY: 1

******************* SOLUTION
'''
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sort
        intervals.sort(key=lambda interval: interval[0])

        latestEndTime = 0

        for index, interval in enumerate(intervals):
            if interval[0] < latestEndTime:
                return False
            if interval[1] > latestEndTime: # NOTE: Don't need this as there shouldn't be more than 1 meeting w/ the same start time as another
                latestEndTime = interval[1]

        return True
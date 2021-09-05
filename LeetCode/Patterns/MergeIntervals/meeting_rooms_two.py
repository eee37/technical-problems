'''
******************* PROBLEM STATEMENT

******************* NOTES
# NOTE: need to make sure a new room wasn't filled before filling. Use a flag
# NOTE: Question to ask interviewer if room vacates at the same time a new one becomes available do we allocate a new room for upcoming meeting. in this case: yes!
# NOTE: append => python equivalent of push

LEETCODE HINT

An important thing to note is that we don't really care which room gets freed up while allocating a room for the current meeting. As long as a room is free, our job is done.

We already know the rooms we have allocated till now and we also know when are they due to get free because of the end times of the meetings going on in those rooms. We can simply check the room which is due to get vacated the earliest amongst all the allocated rooms.

TODO: Go over solution, more optimal

TIME COMPLEXITY: O(N**2)
SPACE COMPLEXITY: O(N)

******************* SOLUTION
'''

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort
        intervals.sort(key=lambda x: x[0])

        rooms = []

        for inter in intervals:
            if rooms:
                newFilled = False
                for index, room in enumerate(rooms):
                    # check availability
                    if inter[0] >= room:  # NOTE: Question to ask interviewer if room vacates at the same time a new one becomes available do we allocate a new room for upcoming meeting. in this case: yes!
                        rooms[index] = inter[1]
                        newFilled = True
                        break
                if not newFilled: rooms.append(
                    inter[1])  # NOTE: need to make sure a new room wasn't filled before filling. Use a flag
            else:
                rooms.append(inter[1])

        return len(rooms)
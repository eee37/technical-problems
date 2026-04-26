import math
"""
    Q: what did we return in the case where she can't eat all the bananas in the H hours? 
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # FIND MAX PILE
        max_pile = max(piles)
        # search_space = range(max_pile) # NOTE: We don't need this

        left = 1 # NOTE: We don't want zero in the search space
        right = max_pile

        if len(piles) > h:
            return None # No solution possible
        ans = max_pile
        while left <= right:
            mid = left + (right - left) // 2
            # if search_space[mid] == 0:
            #     left = mid + 1
            #     continue
            # check whether viable
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            if hours > h:
                left = mid + 1
            else:
                ans = min(ans, mid)
                right = mid -1
        return ans



        